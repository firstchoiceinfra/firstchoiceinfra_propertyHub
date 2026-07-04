from fastapi import FastAPI

from app.routers.admin import router as admin_router
from app.routers.user import router as user_router

app = FastAPI(
    title="FirstChoice Infra PropertyHub",
    version="1.0.0"
)

app.include_router(admin_router)
app.include_router(user_router)


@app.get("/")
def home():
    return {
        "success": True,
        "message": "Welcome to FirstChoice Infra PropertyHub"
    }


@app.get("/health")
def health():
    return {
        "success": True,
        "message": "Server Running Successfully"
    }
