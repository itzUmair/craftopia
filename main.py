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
    return getAllItems()


# URL: localhost:8000/getitem/50001 (50001 is an example product id. you can put any id which is available in our database)
@app.get("/getitem/{item_id}")
async def getitem(item_id):
    return getItem(item_id)


@app.get("/customer/{customer_id}")
def getcustomerdetails(customer_id: int):
    return getCustomerDetail(customer_id)


@app.get("/products/seller/{seller_id}")
def getallproductofseller(seller_id: int):
    return getAllProductOfSeller(seller_id)


@app.get("/products/category/{category_id}")
def getallproductsbycategory(category_id: int):
    return getAllProductsByCategory(category_id)
