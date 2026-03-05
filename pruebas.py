import requests

url = "http://127.0.0.1:8000/tarea-0"

respuesta = requests.get(url)

print(respuesta.json())