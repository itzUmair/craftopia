# This is the main file. This file create a server on which our api runs.

# All the required modules goes here
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder

# getting all the query methods from the database file
from database import *

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# URL: localhost:8000/
@app.get("/")
async def home():
    return {"message": "Connected", "api for": "craftopia", "tech": "fastApi"}


# URL: localhost:8000/getallitems
@app.get("/getallitems")
async def getallitems():
    return {"data": getAllItems()}


# URL: localhost:8000/getitem/50001 (50001 is an example product id. you can put any id which is available in our database)
@app.get("/getitem/{item_id}")
async def getitem(item_id):
    return {"data": getItem(item_id)}
