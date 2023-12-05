import matplotlib.pyplot as plt
import numpy as np


def graficador(CBM, ZM, CBWM, CSBM, name):
    # Crear una figura y ejes para los gráficos
    fig, ax = plt.subplots()
    # Graficar los cuatro arreglos con diferentes colores y etiquetas
    ax.plot(CBM, label='CBM', color='blue')
    ax.plot(ZM, label='ZM', color='green')
    ax.plot(CBWM, label='CBWM', color='red')
    ax.plot(CSBM, label='CSBM', color='purple')

    # Agregar una leyenda
    ax.legend()
    # Configurar etiquetas de los ejes
    ax.set_ylabel('Tiempo Respuesta')
    ax.set_xlabel('Prompt')
    ax.set_ylim(0, 25)
    # Dar un título al gráfico
    ax.set_title('Base de datos ' + name)

    # Mostrar el gráfico
    plt.show()


# Milvus
mCBM = np.array([7, 6, 7, 19, 8, 10, 12, 10, 6, 3])
mZM = np.array([7, 7, 8, 18, 11, 6, 15, 9, 6, 2])
mCBWM = np.array([6, 7, 9, 18, 10, 12, 13, 8, 6, 2])
mCSBM = np.array([8, 8, 8, 15, 12, 8, 16, 11, 10, 6])

# Weaviate
wCBM = np.array([8, 11, 10, 14, 10, 10, 13, 8, 6, 4])
wZM = np.array([7, 10, 10, 19, 15, 12, 12, 7, 9, 4])
wCBWM = np.array([7, 9, 7, 18, 11, 8, 14, 11, 8, 3])
wCSBM = np.array([7, 10, 10, 18, 11, 11, 16, 12, 10, 2])

# Pinecone
pCBM = np.array([8, 11, 8, 19, 7, 15, 11, 9, 8, 5])
pZM = np.array([7, 14, 7, 19, 10, 14, 12, 9, 3])
pCBWM = np.array([8, 12, 8, 22, 12, 12, 14, 9, 14, 6])
pCSBM = np.array([9, 8, 7, 14, 8, 8, 16, 10, 11, 2])

# Faiss
fCBM = np.array([6, 7, 9, 18, 9, 9, 11, 10, 7, 3])
fZM = np.array([6, 7, 9, 19, 11, 6, 8, 9, 7, 4])
fCBWM = np.array([6, 8, 6, 17, 14, 13, 11, 8, 7, 3])
fCSBM = np.array([6, 7, 8, 13, 9, 9, 19, 10, 12, 7])

# Graficar

graficador(mCBM, mZM, mCBWM, mCSBM, 'Milvus')
graficador(wCBM, wZM, wCBWM, wCSBM, 'Weaviate')
graficador(pCBM, pZM, pCBWM, pCSBM, 'Pinecone')
graficador(fCBM, fZM, fCBWM, fCSBM, 'Faiss')


