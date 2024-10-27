from fastapi import FastAPI
from app.routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the School Blog API"}