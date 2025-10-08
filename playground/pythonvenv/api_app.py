from fastapi import FastAPI

app = FastAPI()

@app.get("/") # decorator pattern
def greet():
    return "Hello from FastAPI"

@app.put("/item")
def add_item(item:int):
    return "Item Added"

@app.post("/item")
def update_item():
    return "Item Updated"

@app.get("/item")
def get_item():
    return "Selected Item"

@app.delete("/item")
def delete_item():
    return "Item Deleted"   
     