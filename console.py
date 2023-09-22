from main import *

chat_history = []

yellow = "\033[0;33m"
green = "\033[0;32m"
white = "\033[0;39m"
print(f"{yellow}----------------------------------------------")
print('¡Bienvenido al ChatBot de Entel!')
print('----------------------------------------------')
while True:
    query = input(f"{green}Prompt: ")
    if query == "exit" or query == "quit" or query == "q" or query == "f":
        print('Adiós!')
        sys.exit()
    if query == '':
        continue
    result = qa({"question": query, "chat_history": chat_history})
    print(f"{white}Answer: " + result["answer"])
    chat_history.append((query, result["answer"]))