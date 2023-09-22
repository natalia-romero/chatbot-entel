<h1 style="text-align: center;">ChatBot Entel 📱</h1>
Este chatbot busca asesorar a clientes de Entel acerca de su catalogo de celulares y planes de manera que puedan encontrar lo que mejor se ajuste a sus necesidades.
Se usan las siguientes tecnologias:

- LangChain v0.0.294
- StreamLit v1.24.0
- ChromaDB v0.4.8
- Weaviate v3.24.1

### Instalar Dependencias 
Se deben instalar las siguientes dependencias antes de ejecutar el programa (si es que se necesitan más al ejecutar el programa se indicará lo que falta): 

`` pip install langchain ``

`` pip install chromadb ``

`` pip install weaviate-client ``

`` pip install pysqlite3 ``

`` pip install unstructured ``

`` pip install sentence_transformers ``

`` pip install streamlit ``

### Ejecutar el ChatBot

En primer lugar, antes de ejecutar el ChatBot se deben agregar las api_key necesarias en el archivo .env, por lo que se debe ejecutar el siguiente comando para crear el archivo y  añadir las credenciales:

`` cp .env.example .env ``

Actualmente el ChatBot está disponible por consola y por StreamLit.

#### Consola

Para ejecutarlo por consola:

`` python3 console.py ``

#### StreamLit

Para ejecutarlo por la APP StreamLit:

`` streamlit run stream.py ``

#### Aclaraciones 
El ChatBot está implementado para muchas bases de datos, es por esto que en el archivo **main.py** se debe escoger la base de datos a usar cambiando la siguiente variable:

`` vectorstore = baseDeDatosAUsar()``

El archivo **db.py** cuenta con las funciones de las bases de datos disponibles.

<hr>
<p style="text-align: center;">© 2023 PalaSolutions</p>
<hr>