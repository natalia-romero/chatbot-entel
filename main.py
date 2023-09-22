import streamlit as st
from streamlit_chat import message
from langchain.memory import ConversationBufferMemory
from langchain.chains import (LLMChain, ConversationalRetrievalChain
)
from langchain.chat_models import ChatOpenAI
from pathlib import Path
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from dotenv import load_dotenv
from db import *

load_dotenv()

template = (Path("docs/prompt.txt").read_text()).strip()
#prompt = ChatPromptTemplate.from_template(template)
prompt = PromptTemplate.from_template(template)     

vectorstore = weaviateDB() #seleccionar db (weaviateDB, chromaDB, pineconeDB o milvusDB)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5)
qa = ConversationalRetrievalChain.from_llm(
    model,
    vectorstore.as_retriever(),
    memory=memory,
    #combine_docs_chain_kwargs={"prompt": prompt}
    condense_question_prompt = prompt
)