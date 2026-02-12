from mongo_connection import *
from kafka_publisher import *
import time

init_doc()

def publisher():
    jumps = 0
    size = 30
    warehouse = []
    for docs in colllection.find().skip(jumps).limit(size):
        warehouse.append(docs)
        for w in warehouse:
            send(w)
            time.sleep(0.5)
        jumps += size
        warehouse = []

    if docs in colllection.find():
        for docs in colllection.find():
            send(w)
            time.sleep(0.5)





            