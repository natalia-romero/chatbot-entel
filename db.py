import pandas as pd
import os
import uuid
import sys
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from dotenv import load_dotenv

#Chroma
__import__('pysqlite3')
# se usa modulo pysqlite3 para el uso de chroma
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import chromadb
from langchain.vectorstores import Chroma

#Weaviate
from langchain.vectorstores import Weaviate
import weaviate

#Milivus
from langchain.vectorstores import Milvus

#Pinecone
from langchain.vectorstores import Pinecone
import pinecone

#FAISS
from langchain.vectorstores import FAISS

load_dotenv()

# LEER ARCHIVOS CSV
def getDataFrame(doc):  # función CSV a DataFrame
    df = pd.read_csv(doc)
    return df
planes = getDataFrame("docs/planes.csv")
telefonos = getDataFrame("docs/telefonos.csv")

# CARGAR DOCUMENTOS
loader = DirectoryLoader('docs/', glob="**/*.csv") #  glob="**/*.csv"
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = text_splitter.split_documents(documents) #milvus
embeddings = OpenAIEmbeddings()

# BASES DE DATOS - SE CREA CONEXIÓN Y SE DEBE RETORNAR VECTORSTORE 

def weaviateDB(): #BASE DE DATOS WEAVIATE
    client = weaviate.Client(
        url=os.environ['WEAVIATE-URL'],
        auth_client_secret=weaviate.AuthApiKey(api_key= os.environ['WEAVIATE-API-KEY']), 
    )
    if client.data_object.get()['objects'] != []:
        data = []
    else:
        data = docs
    db = Weaviate.from_documents(data, embeddings, client=client, by_text=False)
    print(client.data_object.get())
    return db

def weaviateDB2():
    # Crear un cliente Weaviate
    client = weaviate.Client()

    # Obtener los nombres de los índices
    index_names = client.get_index_names()

    # Si el índice no existe, crearlo
    index_name = "chatbot"
    if index_name not in index_names:
        client.create_index(index_name, fields=["text"])
        data = docs
        db = Weaviate.from_documents(data, embeddings, client=client, by_text=False)
    else:
        db = weaviate.from_indices([index_name], client=client, by_text=False)

    return db




def chromaDB(): #BASE DE DATOS CHROMA
    client = chromadb.PersistentClient(path="chroma/")
    collection = client.get_or_create_collection(name="docs") 
    print(collection)
    for doc in docs:
        collection.add(
            ids=[str(uuid.uuid1())], metadatas=doc.metadata, documents=doc.page_content
        )
    db = Chroma(client=client, collection_name="docs", embedding_function=embeddings)
    #db = Chroma.from_documents(docs, embeddings)
    return db

def milvusDB(): #BASE DE DATOS MILVUS
    db = Milvus.from_documents(
    docs,
    embeddings,
    connection_args={"host": "localhost", "port": "19530"},
    )
    return db

def pineconeDB(): #BASE DE DATOS PINECONE
    pinecone.init(
        api_key=os.getenv("PINECONE_API_KEY"),  # find at app.pinecone.io
        environment=os.getenv("PINECONE_ENV"),  # next to api key in console
    )
    index = 'chatbot'
    indexes = pinecone.list_indexes()
    if index not in indexes:
        pinecone.create_index(
            name=index,
            metric="cosine",
            dimension=1536)
        db = Pinecone.from_documents(docs, embeddings, index_name=index)
    else:
        db = Pinecone.from_existing_index(index, embeddings)
    return db


def faissDB(): #BASE DE DATOS FAISS
    #os.environ['FAISS_NO_AVX2'] = '1'
    db = FAISS.from_documents(docs, embeddings)
    return db



















# def getDataFrame(doc):  # función para cargar CSV
#     df = pd.read_csv(doc)
#     return df
# pd.read_csv('docs/planes.csv', header=None).T.to_csv('output.csv', header=False, index=False)
# planes = getDataFrame("docs/planes.csv")
# telefonos = getDataFrame("docs/telefonos.csv")
# telefonos = telefonos.fillna('')
# planes = planes.fillna('')

# text_phones = telefonos['0']+' - '+telefonos['1']+' - '+telefonos['2']+' - '+telefonos['3']+' - '+telefonos['4']+' - '+telefonos['5']+' - '+telefonos['6']
# text_planes = planes['0']+' - '+planes['1']+' - '+planes['2']+' - '+planes['3']+' - '+planes['4']+' - '+planes['5']+' - '+planes['6']+' - '+planes['7']

# list_phones=text_phones.tolist() 
# ids_phones= [str(x) for x in telefonos.index.tolist()]
# list_planes=text_planes.tolist() 
# ids_planes= [str(x) for x in planes.index.tolist()]


# client = chromadb.Client()

# collection = client.create_collection(name="example")

# collection.add(
#     documents=[list_phones, list_planes],
#     ids=[str(uuid.uuid1()), str(uuid.uuid1())]
# )

# results = collection.query(
#     query_texts=["iphone"],
#     n_results=2
# )
# print(results)