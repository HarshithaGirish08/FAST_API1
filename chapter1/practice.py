from typing import Optional
from fastapi import FastAPI

#pip install fastapi
#pip install uvicorn[standard]
#uvicorn name:app --reload

app = FastAPI()
@app.get("/")
async def simple_api():
    return{"message" : "welcome to fast api"}