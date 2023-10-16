import re
import matplotlib.pyplot as plt
archivo_entrada = 'time.txt'


avg = []
# Abre el archivo de entrada en modo lectura y el archivo de salida en modo escritura
with open(archivo_entrada, 'r') as entrada:
    for linea in entrada:
        matches = re.search(r'\[([\d,\s]+)\] - Promedio: ([\d.]+)', linea)
        if matches:
            lista_de_numeros = [int(num) for num in matches.group(1).split(',')]
            promedio = float(matches.group(2))
            print("Promedio:", promedio)
            avg.append(promedio)
print(avg)
import re
import matplotlib.pyplot as plt

archivo_entrada = 'time.txt'

avg = []

# Abre el archivo de entrada en modo lectura
with open(archivo_entrada, 'r') as entrada:
    for linea in entrada:
        matches = re.search(r'\[([\d,\s]+)\] - Promedio: ([\d.]+)', linea)
        if matches:
            promedio = float(matches.group(2))
            avg.append(promedio)

# Crear una lista de índices para los valores en avg
indices = range(len(avg))

# Crear un gráfico de líneas
plt.plot(indices, avg, marker='o', linestyle='-', color='darkblue')

# Etiquetar el eje x con los índices
plt.xticks(indices)

# Etiquetas de los ejes
plt.xlabel('Chat number')
plt.ylabel('Response in seconds')

# Título del gráfico
plt.title('Time response')

# Mostrar el gráfico de líneas
plt.show()

promedio = sum(avg) / len(avg)
print(promedio)