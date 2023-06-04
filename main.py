# This is the main file. This file create a server on which our api runs.

# All the required modules goes here
from fastapi import FastAPI, Request
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
@app.get("/product/getitem/{item_id}")
async def getitem(item_id):
    return getItem(item_id)


@app.get("/customer/{customer_id}")
async def getcustomerdetails(customer_id: int):
    return getCustomerDetail(customer_id)


@app.get("/products/seller/{seller_id}")
async def getallproductofseller(seller_id: int):
    return getAllProductOfSeller(seller_id)


@app.get("/products/category/{category_id}")
async def getallproductsbycategory(category_id: int):
    return getAllProductsByCategory(category_id)


@app.get("/products/search/{product_name}")
async def getsearchedproduct(product_name: str):
    return getSearchedProduct(product_name)


@app.patch("/seller/updateprofile/{seller_id}")
async def sellerupdateprofile(seller_id: int, request: Request):
    try:
        req = await request.json()
        return sellerUpdateProfile(seller_id, req)
    except:
        return {"message": "invalid request"}


@app.patch("/customer/updateprofile/{customer_id}")
async def customerupdateprofile(customer_id: int, request: Request):
    try:
        req = await request.json()
        return customerUpdateProfile(customer_id, req)
    except:
        return {"message": "invalid request"}


@app.patch("/order/ship/{order_id}")
async def shippedOrder(order_id: int):
    return setShippedOrder(order_id)


@app.patch("/order/complete/{order_id}")
async def shippedOrder(order_id: int):
    return setCompletedOrder(order_id)


@app.put("/product/addproduct/{seller_id}")
async def addproduct(seller_id: int, request: Request):
    try:
        req = await request.json()
        return addProduct(seller_id, req)
    except:
        return {"message": "invalid request"}


@app.delete("/product/deleteproduct/{product_id}")
async def removeproduct(product_id: int):
    return removeProduct(product_id)


@app.patch("/product/updateproduct/{product_id}")
async def updateproduct(product_id: int, request: Request):
    try:
        req = await request.json()
        return updateProduct(product_id, req)
    except:
        return {"message": "invalid request"}


@app.put("/customer/signup")
async def customersignup(request: Request):
    try:
        req = await request.json()
        return customerSignup(req)
    except:
        return {"message": "invalid request"}


@app.put("/seller/signup")
async def sellersignup(request: Request):
    try:
        req = await request.json()
        return sellerSignup(req)
    except:
        return {"message": "invalid request"}


@app.post("/customer/login")
async def customerlogin(request: Request):
    try:
        req = await request.json()
        return customerLogin(req)
    except:
        return {"message": "invalid request"}
