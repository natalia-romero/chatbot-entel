
import os
from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationBufferWindowMemory
from langchain.memory import ConversationSummaryBufferMemory
from langchain.memory import ZepMemory
from langchain.llms import OpenAI
from dotenv import load_dotenv
from uuid import uuid4
load_dotenv()


def CBM():
    return ConversationBufferMemory(memory_key="chat_history", return_messages=True)
def ZM():
    session_id = str(uuid4())
    return ZepMemory(session_id=session_id,url=os.getenv("ZEP_API_URL"),memory_key="chat_history",return_messages=True)
def CBWM():
    return ConversationBufferWindowMemory(k=6, memory_key="chat_history", return_messages=True)
def CSBM():
    return ConversationSummaryBufferMemory(llm=OpenAI(temperature=0),  max_token_limit=2000, memory_key="chat_history", ai_prefix="Ejecutivo Entel", human_prefix="Usuario", return_messages=True)

