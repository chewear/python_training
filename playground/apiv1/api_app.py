from fastapi import FastAPI
from controller.address_book_api import router as address_book_router

app = FastAPI()
app.include_router(address_book_router)

@app.get("/") # decorator pattern
def greet():
    return "Hello from FastAPI"
  