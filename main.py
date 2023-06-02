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


@app.get("/customer/{customer_id}")
def getCustomerDetails(customer_id: int):
    cursor = db.cursor()
    sql = "SELECT CONCAT(fname,' ',lname) as 'Customer Name', address, email FROM customer WHERE customer_id = %s"
    values = (customer_id,)
    cursor.execute(sql, values)
    customer = cursor.fetchone()
    if customer:
        return customer
    else:
        return {"message": "customer not found"}


@app.get("/products/seller/{seller_id}")
def getAllProductsOfSeller(seller_id: int):
    cursor = db.cursor()
    sql = "SELECT product_name, price_per_unit, stock_in_inventory FROM product WHERE seller_id = %s"
    values = (seller_id,)
    cursor.execute(sql, values)
    products = cursor.fetchall()
    return products


@app.get("/products/category/{category_id}")
def getAllProductsByCategory(category_id: int):
    cursor = db.cursor()
    sql = "SELECT product_name, price_per_unit, stock_in_inventory FROM product WHERE category_id = %s"
    values = (category_id,)
    cursor.execute(sql, values)
    products = cursor.fetchall()
    return products
