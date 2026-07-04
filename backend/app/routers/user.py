from fastapi import APIRouter
from app.schemas.user import UserRegistration
from app.auth.user_auth import UserAuth

router = APIRouter(
    prefix="/user",
    tags=["User"]
)
