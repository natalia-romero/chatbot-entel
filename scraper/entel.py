import requests
from bs4 import BeautifulSoup

# Realizar la solicitud HTTP
url = "https://miportal.entel.cl/personas/catalogo/celulares"
response = requests.get(url)

# Crear el objeto BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.find_all('main', id_='productInfo'))
