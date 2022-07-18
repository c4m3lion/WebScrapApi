from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
import tapaz;   

app = FastAPI()

@app.get("/")
def read_root():
    return tapaz.getTapazItems();


@app.get("/tapaz/")
def read_item():
    return tapaz.getTapazItems();
