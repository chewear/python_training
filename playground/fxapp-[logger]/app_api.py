from fastapi import FastAPI
from controller.fx_api_controller import router as fx_api_router

app = FastAPI()
app.include_router(fx_api_router)

@app.get("/")
def greet():
    return "Server is UP"
  