import requests

# Local
# url = "http://127.0.0.1:8000/"

# Remoto en Render
url = "https://tarea-0-1dwn.onrender.com/"

respuesta = requests.get(url)
print(respuesta.json())