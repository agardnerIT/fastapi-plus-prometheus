from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import random

app = FastAPI()

@app.get("/", response_class=JSONResponse)
def get_homepage():

    random_number = random.randint(a=0, b=100)

    return {"status": "ok", "random_number": random_number}
