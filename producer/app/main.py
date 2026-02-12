from mongo_connection import *
from kafka_publisher import *


init_doc()

def publisher():
    warehouse = []
    for docs in colllection.find().skip(30).limit(30):
        warehouse.append(docs)
        for w in warehouse:
            send(w)
    




               