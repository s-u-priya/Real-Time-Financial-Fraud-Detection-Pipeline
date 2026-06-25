from kafka import KafkaProducer
import pandas as pd
import json
import time


producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x:
    json.dumps(x).encode('utf-8')
)


df = pd.read_csv("data/paysim.csv")


for index, row in df.iterrows():

    transaction = row.to_dict()

    producer.send(
        "transactions",
        transaction
    )

    print(
        f"Sent {index}"
    )

    time.sleep(0.05)


producer.flush()

print("Finished")