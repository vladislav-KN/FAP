import json

from fastapi import FastAPI

app = FastAPI()


@app.get("/gui/{id}")
async def root(id: str):
    print(id)
    with open("data.json", "r") as f:
        ret = json.load(f)
    return ret
@app.get("/orders/{id}")
async def root(id: str):
    print(id)
    with open("order.json", "r") as f:
        ret = json.load(f)
    return ret
@app.get("/settings/{id}")
async def root(id: str):
    print(id)
    with open("settings.json", "r") as f:
        ret = json.load(f)
    return ret
@app.get("/order/{id}")
async def root(id: str):
    print(id)
    return {"orders": [1,2,3,4]}

