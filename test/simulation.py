import datetime
import time
from chats import *
from main import *

x = 0
with open('chat.txt', 'w') as f:
    for i in range(100):
        print('- - - - - - - - - - - - ITERACION '+str(i)+' - - - - - - - - - - - -')
        chat = chats[x]
        chat_history = []
        times = []
        text = '- - - - - - Chat ' + str(x) + ' - - - - - -'
        f.write(text+'\n')
        print(text)
        for k in chat:
            print("- [[Consulta]]: " + k)
            first_time = datetime.datetime.now()
            result = qa({"question": k, "chat_history": chat_history})
            later_time = datetime.datetime.now()
            delta = int((later_time - first_time).total_seconds())
            times.append(delta)
            print("- - [[Respuesta]]: " + result["answer"])
            chat_history.append((k, result["answer"]))
            f.write('[[Consulta]]: \n'+k+'\n')
            f.write('[[Respuesta]]: \n'+result["answer"]+'\n')
        print("Tiempos de respuesta: ", times)
        print("Promedio de respuesta: ", sum(times) / len(times))
        f.write('[[Tiempos: '+str(times)+' - Promedio: '+str(sum(times) / len(times))+']]\n')
        memory.clear()
        x = (x + 1) % 5
        time.sleep(3) 