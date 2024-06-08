from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI
import joblib
from pathlib import Path
import pandas as pd

app = FastAPI()


@app.get("/")
def read_root():
    return {"response": "Ready!"}

