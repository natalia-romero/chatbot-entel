import pandas as pd
import os
import sys
import weaviate
__import__('pysqlite3')
# se usa modulo pysqlite3 para el uso de chroma
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
from langchain.vectorstores import Weaviate
from dotenv import load_dotenv
load_dotenv()

# LEER ARCHIVOS CSV
def getDataFrame(doc):  # función CSV a DataFrame
    df = pd.read_csv(doc)
    return df
planes = getDataFrame("docs/planes.csv")
telefonos = getDataFrame("docs/telefonos.csv")

# CARGAR DOCUMENTOS
loader = DirectoryLoader('docs/') #  glob="**/*.csv"
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = text_splitter.split_documents(documents)
embeddings = OpenAIEmbeddings()

# BASES DE DATOS - SE CREA CONEXIÓN Y SE DEBE RETORNAR VECTORSTORE 

def weaviateDB(): #BASE DE DATOS WEAVIATE
    client = weaviate.Client(
        url=os.environ['WEAVIATE-URL'],
        auth_client_secret=weaviate.AuthApiKey(api_key= os.environ['WEAVIATE-API-KEY']), 
    )
    db = Weaviate.from_documents(docs, embeddings, client=client, by_text=False)
    return db

def chromaDB(): #BASE DE DATOS CHROMA
    db = Chroma.from_documents(docs, embeddings)
    return db

# def milvusDB(): #BASE DE DATOS MILVUS
#     #conexion y return de la db

# def pineConeDB(): #BASE DE DATOS PINECONE
#     #conexion y return de la db

























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