from fastapi import FastAPI

app = FastAPI()

# Endpoint raíz
@app.get("/")
def root():
    return {"respuesta": "Primer tarea realizada"}

# Opcional: mantener tu endpoint original
@app.get("/tarea-0")
def tarea_0():
    return {"respuesta": "Primer tarea realizada"}