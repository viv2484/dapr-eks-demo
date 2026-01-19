from fastapi import FastAPI

# app = FastAPI()

# @app.post("/orders")
# def receive(order: dict):
#     print("Received order:", order)
#     return {"status": "processed"}

from fastapi import FastAPI
from dapr.ext.fastapi import DaprApp

app = FastAPI()
dapr_app = DaprApp(app)

@dapr_app.subscribe(pubsub_name="order-pubsub", topic="orders")
async def handle_order(data: dict):
    print(f"Received order: {data}")
    return {"status": "ok"}

