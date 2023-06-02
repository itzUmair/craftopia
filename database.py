# This file handles all the tasks related to the mySQL database
# This file creates connection with the database and runs all the queries


import mysql.connector
from queries import *


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


# this is a helper function to reduce redundant code. this creates a cursor in our database from where the queries are to be ran
def execute(query, params=None):
    cursor = db.cursor()
    cursor.execute(query, params)
    return cursor.fetchall()


# get all the available items in the database
def getAllItems():
    cursor = db.cursor()
    cursor.execute(getAllItemQuery)
    return {"data": cursor.fetchall()}


# get the specific item that is provided through the url
def getItem(item_id):
    params = (item_id,)
    cursor = db.cursor()
    cursor.execute(getItemQuery, params)
    return {"data": cursor.fetchone()}


def getCustomerDetail(customer_id: int):
    cursor = db.cursor()
    params = (customer_id,)
    cursor.execute(getCustomerDetailQuery, params)
    customer = cursor.fetchone()
    if customer:
        return {"data": customer}
    else:
        return {"message": "customer not found"}


def getAllProductOfSeller(seller_id: int):
    cursor = db.cursor()
    params = (seller_id,)
    cursor.execute(getAllProductOfSellerQuery, params)
    products = cursor.fetchall()
    if products:
        return {"data": products}
    else:
        return {"message": "no products"}


def getAllProductsByCategory(category_id):
    cursor = db.cursor()
    params = (category_id,)
    cursor.execute(getAllProductsByCategoryQuery, params)
    products = cursor.fetchall()
    if products:
        return {"data": products}
    else:
        return {"message": "no products found in this category"}
