import requests
import csv
from bs4 import BeautifulSoup

# Archivo destino
archivo_csv = "../csv/planes.csv"

# Request HTTP
url = "https://www.entel.cl/planes/oferta-portabilidad/"
response = requests.get(url)

# Objeto BS4
soup = BeautifulSoup(response.content, 'html.parser')

print ("Obteniendo datos de la pagina https://www.entel.cl/planes/oferta-portabilidad/ ...")

# Obtener el elemento con id "rootProductInfo_JSON"
plan_info = soup.find(class_="table table-planes")

if plan_info:
    # Obtener los elementos de la tabla de planes
    filas = plan_info.find_all('tr')

    # Matriz para los planes
    planes = []

    print("Obteniendo datos desde HTML...")
    # Iterar sobre las filas y extraer los datos
    for fila in filas:
        celdas = fila.find_all(['th', 'td'])
        fila_datos = [celda.get_text(strip=True) for celda in celdas]
        planes.append(fila_datos)

    print("Escrbiendo csv en ../csv/planes.csv ...")
    # Escribir la matriz en el archivo CSV
    with open(archivo_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(planes)

    print("Archivo CSV generado exitosamente.")
else:
    print("No se pudo obtener los datos de la pagina")