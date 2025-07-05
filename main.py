from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numeros(BaseModel):
    a: float
    b: float

@app.post("/soma")

def somar(numeros: Numeros):
    resultado = numeros.a + numeros.b
    return {"resultado": resultado}
