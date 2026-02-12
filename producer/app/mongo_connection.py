from pymongo import MongoClient
import json

client = MongoClient("mongodb://mongodb:27017")

db = client.test_17
colllection = db.customers_orders

def init_doc():
    if colllection.count_documents({}) == 0:
        with open("producer\app\suspicious_customers_orders.json") as f:
            data = json.load(f)
        colllection.insert_many(data)
        

