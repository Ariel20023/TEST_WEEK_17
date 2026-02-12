import json
from mongo import insert_in_mongo,insert_in_mongo_many
from confluent_kafka import Consumer
from datetime import datetime


consumer_config = {
    "bootstrap.servers": "kafka:9092",
    "group.id": "test_17",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(consumer_config)

consumer.subscribe(["test_17"])

print("🟢 Consumer is running and subscribed to orders topic")

try:
    while True:
        msg = consumer.poll(0.5)
        if msg is None:
            continue
        if msg.error():
            print("❌ Error:", msg.error())
            continue

        value = msg.value().decode("utf-8")
        order = json.loads(value)
        print(f"📦 Received order:",order)
        insert_in_mysql(order)
except KeyboardInterrupt:
    print("\n🔴 Stopping consumer")

finally:
    consumer.close()