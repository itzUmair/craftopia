# This file handles all the tasks related to the mySQL database
# This file creates connection with the database and runs all the queries
import mysql.connector
from queries import *
import bcrypt
from dotenv import load_dotenv
import os
import datetime
import jwt


load_dotenv()

jwtsecret = os.getenv("JWT_SECRET")


# create connection with the database
def connectDB():
    DB = mysql.connector.connect(
        host="localhost",  # this will remain same for all of us as our database is not hosted online
        user="root",  # change this to whatever username you set while installing mySQL database
        password="86247",  # change this to the password you set for the username
        database="craftopia",  # this will remain same as long as you have created the database through the schema I provided
    )
    cursor = DB
    return cursor


# this creates the connection with the database
print("connecting to database")
db = connectDB()
print("connected to Craftopia database")


# ==================================== QUERIES ==================================================


def verifyToken(headers):
    try:
        authorization_header = headers.get("authorization")
        if authorization_header is None:
            return {"success": True, "message": "token missing"}
        token = authorization_header.split(" ")[1]
        decoded_token = jwt.decode(token, jwtsecret, algorithms=["HS256"])
        return decoded_token
    except jwt.ExpiredSignatureError:
        return {"success": False, "message": "token expired"}
    except (jwt.DecodeError, IndexError):
        return {"success": False, "message": "invalid token"}


# this is a helper function to reduce redundant code. this creates a cursor in our database from where the queries are to be ran
def execute(query, params=None):
    cursor = db.cursor(buffered=True)
    cursor.execute(query, params)
    return cursor.fetchall()


# get all the available items in the database
def getAllItems():
    cursor = db.cursor()
    cursor.execute(getAllItemQuery)
    return {"data": cursor.fetchall()}


# get the specific item that is provided through the url
def getItem(item_id):
    db.reconnect()
    cursor = db.cursor()
    params = (item_id,)
    cursor.execute(getItemQuery, params)
    return {"data": cursor.fetchone()}


def getCustomerDetail(customer_id: int, requestHeaders):
    db.reconnect()
    cursor = db.cursor()
    validation = verifyToken(requestHeaders)
    if validation.get("success") == False:
        return validation
    params = (customer_id,)
    cursor.execute(getCustomerDetailQuery, params)
    customer = cursor.fetchone()
    if customer:
        return {"data": customer}
    else:
        return {"message": "customer not found"}


def getAllProductOfSeller(seller_id: int):
    db.reconnect()
    cursor = db.cursor()
    params = (seller_id,)
    cursor.execute(getAllProductOfSellerQuery, params)
    products = cursor.fetchall()
    if products:
        return {"data": products}
    else:
        return {"message": "no products"}


def getAllProductsByCategory(category_id):
    db.reconnect()
    cursor = db.cursor()
    params = (category_id,)
    cursor.execute(getAllProductsByCategoryQuery, params)
    products = cursor.fetchall()
    if products:
        return {"data": products}
    else:
        return {"message": "no products found in this category"}


def getSearchedProduct(product_name):
    db.reconnect()
    cursor = db.cursor()
    params = (f"%{product_name}%",)
    cursor.execute(getSearchedProductQuery, params)
    products = cursor.fetchall()
    if products:
        return {"data": products}
    else:
        return {"message": "no products found by this name"}


def sellerUpdateProfile(seller_id: int, request, requestHeaders):
    cursor = db.cursor()
    validation = verifyToken(requestHeaders)
    if validation.get("success") == False:
        return validation
    fname = request["fname"].capitalize()
    lname = request["lname"].capitalize()
    username = request["username"]
    phone = request["phone"]
    email = request["email"]
    password = request["password"]
    params = (fname, lname, username, phone, email, password, seller_id)
    cursor.execute(sellerUpdateProfileQuery, params)
    db.commit()
    if cursor.rowcount:
        return {"message": "Seller information updated successfully"}
    else:
        return {"message": "already up-to-date"}


def customerUpdateProfile(customer_id: int, request, requestHeaders):
    cursor = db.cursor()
    validation = verifyToken(requestHeaders)
    if validation.get("success") == False:
        return validation
    fname = request["fname"].capitalize()
    lname = request["lname"].capitalize()
    address = request["address"]
    email = request["email"]
    password = request["password"]
    params = (fname, lname, address, email, password, customer_id)
    cursor.execute(customerUpdateProfileQuery, params)
    db.commit()
    if cursor.rowcount:
        return {"message": "Customer information updated successfully"}
    else:
        return {"message": "already up-to-date"}


def setShippedOrder(order_id: int, requestHeaders):
    cursor = db.cursor()
    validation = verifyToken(requestHeaders)
    if validation.get("success") == False:
        return validation
    params = (order_id,)
    cursor.execute(setShippedOrderQuery, params)
    db.commit()
    if cursor.rowcount:
        return {"message": "Order Shipped"}
    else:
        return {"message": "already up-to-date"}


def setCompletedOrder(order_id: int, requestHeaders):
    cursor = db.cursor()
    validation = verifyToken(requestHeaders)
    if validation.get("success") == False:
        return validation
    params = (order_id,)
    cursor.execute(setCompletedOrderQuery, params)
    db.commit()
    if cursor.rowcount:
        return {"message": "Order Completed"}
    else:
        return {"message": "already up-to-date"}


def addProduct(seller_id, request, reqHeaders):
    cursor = db.cursor()
    validation = verifyToken(requestHeaders)
    if validation.get("success") == False:
        return validation
    product_name = request["product_name"].title()
    price_per_unit = request["price_per_unit"]
    stock_in_inventory = request["stock_in_inventory"].capitalize()
    category_id = request["category_id"]
    params = (product_name, price_per_unit, stock_in_inventory, category_id, seller_id)
    cursor.execute(addProductQuery, params)
    db.commit()
    return {"message": "Added product successfully"}


def removeProduct(product_id, requestHeaders):
    cursor = db.cursor()
    validation = verifyToken(requestHeaders)
    if validation.get("success") == False:
        return validation
    params = (product_id,)
    cursor.execute(deleteProductQuery, params)
    db.commit()
    if cursor.rowcount:
        return {"message": "Product removed successfully"}
    else:
        return {"message": "no product found"}


def updateProduct(product_id, request, requestHeaders):
    cursor = db.cursor()
    validation = verifyToken(requestHeaders)
    if validation.get("success") == False:
        return validation
    product_name = request["product_name"].title()
    price_per_unit = request["price_per_unit"]
    stock_in_inventory = request["stock_in_inventory"].capitalize()
    category_id = request["category_id"]
    params = (product_name, price_per_unit, stock_in_inventory, category_id, product_id)
    cursor.execute(updateProductQuery, params)
    db.commit()
    if cursor.rowcount:
        return {"message": "Product updated successfully"}
    else:
        return {"message": "already up-to-date"}


def customerSignup(request):
    cursor = db.cursor()
    fname = request["fname"].capitalize()
    lname = request["lname"].capitalize()
    email = request["email"]
    address = request["address"]
    password = request["password"]
    tempParams = (email,)
    cursor.execute(findCustomerAccountQuery, tempParams)
    if len(cursor.fetchall()) >= 1:
        return {"message": "account with this email already exists."}
    passwordBytes = password.encode("utf-8")
    hashedPassword = bcrypt.hashpw(passwordBytes, bcrypt.gensalt()).decode("utf-8")
    params = (
        fname,
        lname,
        address,
        email,
        hashedPassword,
    )
    result = cursor.execute(createCustomerAccountQuery, params)
    db.commit()
    if cursor.rowcount:
        return {"message": "account created successfully"}
    else:
        return {"message": "something went wrong"}


def sellerSignup(request):
    cursor = db.cursor()
    fname = request["fname"].capitalize()
    lname = request["lname"].capitalize()
    email = request["email"]
    username = request["username"]
    password = request["password"]
    phone = request["phone"]
    tempParams = (
        email,
        phone,
        username,
    )
    cursor.execute(findSellerAccountQuery, tempParams)
    if len(cursor.fetchall()) >= 1:
        return {"message": "account with these credentials already exists."}
    passwordBytes = password.encode("utf-8")
    hashedPassword = bcrypt.hashpw(passwordBytes, bcrypt.gensalt()).decode("utf-8")
    params = (
        fname,
        lname,
        username,
        phone,
        email,
        hashedPassword,
    )
    print("here")
    result = cursor.execute(createSellerAccountQuery, params)
    db.commit()
    if cursor.rowcount:
        return {"message": "account created successfully"}
    else:
        return {"message": "something went wrong"}


def customerLogin(request):
    cursor = db.cursor()
    email = request["email"]
    password = request["password"]
    params = (email,)
    cursor.execute(loginCustomerQuery, params)
    result = cursor.fetchall()
    if len(result) == 0:
        return {"message": "no account found"}
    passwordBytes = password.encode("utf-8")
    verifyPassword = bcrypt.checkpw(passwordBytes, result[0][-1].encode("utf-8"))
    if not verifyPassword:
        return {"message": "invalid password"}

    customerData = {
        "c_name": result[0][1] + result[0][2],
        "c_address": result[0][3],
        "c_email": result[0][4],
        "c_authority": "customer",
    }

    data = {
        "c_id": result[0][0],
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24),
    }

    jwtToken = jwt.encode(data, jwtsecret, algorithm="HS256")
    return {"message": "success", "token": jwtToken, "data": customerData}


def sellerLogin(request):
    cursor = db.cursor()
    email = request["email"]
    password = request["password"]
    params = (email,)
    cursor.execute(loginSellerQuery, params)
    result = cursor.fetchall()
    if len(result) == 0:
        return {"message": "no account found"}
    passwordBytes = password.encode("utf-8")
    verifyPassword = bcrypt.checkpw(passwordBytes, result[0][-1].encode("utf-8"))
    if not verifyPassword:
        return {"message": "invalid password"}

    customerData = {
        "s_name": result[0][1] + result[0][2],
        "s_address": result[0][3],
        "s_email": result[0][4],
        "s_authority": "seller",
    }

    data = {
        "s_id": result[0][0],
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24),
    }

    jwtToken = jwt.encode(data, jwtsecret, algorithm="HS256")
    return {"message": "success", "token": jwtToken, "data": customerData}


def getAllProductsCoverImage():
    db.reconnect()
    cursor = db.cursor()
    cursor.execute(getAllProductsCoverImageQuery)
    images = cursor.fetchall()
    if images:
        return {"data": images}
    else:
        return {"message": "no images"}


def getSearchedProductsCoverImage(product_name):
    db.reconnect()
    cursor = db.cursor()
    params = (f"%{product_name}%",)
    cursor.execute(getSearchedProductsCoverImageQuery, params)
    images = cursor.fetchall()
    if images:
        return {"data": images}
    else:
        return {"message": "no images"}


def getCategoryProductsCoverImage(category_id):
    db.reconnect()
    cursor = db.cursor()
    params = (category_id,)
    cursor.execute(getCategoryProductsCoverImageQuery, params)
    images = cursor.fetchall()
    if images:
        return {"data": images}
    else:
        return {"message": "no images"}


def getProductDetailsImages(item_id):
    db.reconnect()
    cursor = db.cursor()
    params = (item_id,)
    cursor.execute(getProductDetailsImagesQuery, params)
    images = cursor.fetchall()
    if images:
        return {"data": images}
    else:
        return {"message": "no images"}


def getSimilarProducts(category_id, currentProductId):
    db.reconnect()
    cursor = db.cursor()
    params = (
        category_id,
        currentProductId,
    )
    cursor.execute(getSimilarProductsQuery, params)
    products = cursor.fetchall()
    if products:
        return {"data": products}
    else:
        return {"message": "no products"}


def getSimilarProductsCoverImages(category_id, currentProductId):
    db.reconnect()
    cursor = db.cursor()
    params = (
        category_id,
        currentProductId,
    )
    cursor.execute(getSimilarProductsCoverImagesQuery, params)
    products = cursor.fetchall()
    if products:
        return {"data": products}
    else:
        return {"message": "no products"}


def placeOrder():
    pass
