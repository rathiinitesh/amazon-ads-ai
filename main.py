from fastapi import FastAPI

from app.api.v1.api import api_router
from app.api.v1.user import router as user_router

app = FastAPI(title="Amazon Ads AI ChatBot", version="1.0.0")

app.include_router(api_router, prefix="/api/v1")
app.include_router(user_router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "Amazon Ads AI ChatBot API is running."}
