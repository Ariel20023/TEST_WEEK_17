from pymongo import MongoClient
import json

client = MongoClient("mongodb://mongodb:27017")

db = client.test_17
colllection = db.customers_orders

def init_doc():
    if colllection.count_documents({}) == 0:
        with open("producer\app\suspicious_customers_orders.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        colllection.insert_many(data)
        


# batch_size = 30
# offset = 0

# while True:
#     batch = load_batch(collection, batch_size, offset)

#     if not batch:   
#         break

#     for doc in batch:
#         send_to_kafka(doc)
#         time.sleep(0.5)

#     offset += batch_size