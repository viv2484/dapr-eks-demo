from fastapi import FastAPI

app = FastAPI()

@app.post("/orders")
def receive(order: dict):
    print("Received order:", order)
    return {"status": "processed"}
