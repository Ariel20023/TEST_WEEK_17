from confluent_kafka import Producer
import json



def delivery_report(err, msg):
    if err:
        print(f"❌ Delivery failed: {err}")
    else:
        print(f"✅ Delivered {msg.value().decode('utf-8')}")
        print(f"✅ Delivered to {msg.topic()} : partition {msg.partition()} : at offset {msg.offset()}")




def send(doc):
    
    producer_config = {
        "bootstrap.servers": "kafka:9092"
    }

    producer = Producer(producer_config)

    data = doc.model_dump()
    data["user_id"] = str(data["user_id"])
    value = json.dumps(data).encode("utf-8")    
    producer.produce(
        topic="test_17",
        value=value,
        callback=delivery_report
        )
    producer.poll(0.5)
    producer.flush()