
from fastapi import FastAPI

app = FastAPI(
    title="FirstChoice Infra PropertyHub",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to FirstChoice Infra PropertyHub"
    }

@app.get("/health")
def health():
    return {
        "status": "Server Running"
    }
