import streamlit as st
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from pathlib import Path
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from db import *

load_dotenv()

template = Path("docs/prompt.txt").read_text()
prompt = ChatPromptTemplate.from_template(template)

vectorstore = weaviateDB() #seleccionar db (weaviateDB, chromaDB, pineconeDB o milvusDB)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
print(memory)
model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5)
qa = ConversationalRetrievalChain.from_llm(
    model,
    vectorstore.as_retriever(),
    memory=memory,
    combine_docs_chain_kwargs={"prompt": prompt}
)

query = "nunca he usado iphone y quiero comprarme uno nuevo, cual me recomendarías?"
result = qa({"question": query})

print(result["answer"])
