import datetime
from main import *
chat_history = []

yellow = "\033[0;33m"
green = "\033[0;32m"
white = "\033[0;39m"
print(f"{yellow}----------------------------------------------")
print('¡Bienvenido al ChatBot de Entel!')
print('----------------------------------------------')
time = []
while True:
    query = input(f"{green}Pregunta: ")
    if query == "exit" or query == "quit" or query == "q" or query == "f":
        print('Adiós!')
        print("Tiempos de respuesta: ",time)
        print("Promedio de respuesta: ",sum(time) / len(time))
        sys.exit()
    if query == '':
        continue
    first_time = datetime.datetime.now()
    result = qa({"question": query, "chat_history": chat_history})
    later_time = datetime.datetime.now()
    delta = int((later_time - first_time).total_seconds())
    time.append(delta)
    print(f"{white}Respuesta: " + result["answer"])
    chat_history.append((query, result["answer"]))