from fastapi import FastAPI
from .validation import validate

app = FastAPI()

@app.post("/referee/validate")
def referee_validate(request: dict):
    return validate(request)
