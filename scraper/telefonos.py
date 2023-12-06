import requests
import re
import csv
from bs4 import BeautifulSoup

# Archivo destino
archivo_csv = "phones.csv"
headers = ["marca", "nombre", "precio", "almacenamiento", "pantalla", "camara", "productId"]
objetos = []
for i in range(10):
    # Request HTTP
    url = "https://miportal.entel.cl/personas/catalogo/celulares/page/" + str(i+1)
    response = requests.get(url)

    # Objeto BS4
    soup = BeautifulSoup(response.content, 'html.parser')

    # Obtener el elemento con id "rootProductInfo_JSON"
    product_info = soup.find(id="rootProductInfo_JSON")

    # Obtener el contenido de texto de
    text_content = product_info.get_text()

    # Obtener los indices donde aparecen los atributos
    indices = []
    inicio = 0
    while True:
        index = text_content.find("attributes\": {", inicio)
        if index == -1:
            break
        indices.append(index)
        inicio = index + 1

    # Separar por los indices anteriores y guardarlo en una lista
    contents = []
    for i in range(len(indices)):
        start = indices[i]
        end = indices[i + 1] if i + 1 < len(indices) else len(text_content)
        contents.append(text_content[start:end])

    print(contents)
    # Obtener los valores que necesitamos de cada elemento de la lista
    marcas = []
    nombres = []
    precios = []
    almacenamientos = []
    pantallas = []
    camaras = []
    productIds = []
    for content in contents:
        marca = r'"brand": \["(.*?)"\]'
        matches = re.findall(marca, content)
        marcas.extend(matches)

        nombre = r'"displayName": \["(.*?)"\]'
        matches = re.findall(nombre, content)
        nombres.extend(matches)

        precio = r'"price.formatted": \["(.*?)"\]'
        matches = re.findall(precio, content)
        precios.extend(matches)

        almacenamiento = r'"internal": \["(.*?)"\]'
        matches = re.findall(almacenamiento, content)
        almacenamientos.extend(matches)

        pantalla = r'"product.screenSize": \["(.*?)"\]'
        matches = re.findall(pantalla, content)
        pantallas.extend(matches)

        camara = r'"primaryFromProduct": \["(.*?)"\]'
        matches = re.findall(camara, content)
        camaras.extend(matches)

        productId = r'"productId": \["(.*?)"\]'
        matches = re.findall(productId, content)
        productIds.extend(matches)

    for marca, nombre, precio, almacenamiento, pantalla, camara, productId in zip(marcas, nombres, precios, almacenamientos,
                                                                    pantallas, camaras, productIds):
        objeto = {
            "marca": marca,
            "nombre": nombre,
            "precio": precio,
            "almacenamiento": almacenamiento,
            "pantalla": pantalla,
            "camara": camara,
            "productId": productId
        }
        objetos.append(objeto)
