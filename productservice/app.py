from fastapi import FastAPI
import requests
import os

app = FastAPI()

DAPR_PORT = os.getenv("DAPR_HTTP_PORT", "3500")
PUBSUB_NAME = "order-pubsub"
TOPIC_NAME = "orders"

@app.post("/publish")
def publish(order: dict):
    url = f"http://localhost:{DAPR_PORT}/v1.0/publish/{PUBSUB_NAME}/{TOPIC_NAME}"
    requests.post(url, json=order)
    return {"message": "Order published"}
