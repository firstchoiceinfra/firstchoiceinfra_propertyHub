from fastapi import APIRouter
from pydantic import BaseModel

from app.auth.user_login import UserLoginService

router = APIRouter(
    prefix="/login",
    tags=["User Login"]
)


# REQUEST MODELS
class LoginRequest(BaseModel):
    mobile_number: str


class VerifyRequest(BaseModel):
    mobile_number: str
    otp: int


# SEND OTP FOR LOGIN
@router.post("/send-otp")
def send_login_otp(data: LoginRequest):

    return UserLoginService.login_with_otp(data.mobile_number)


# VERIFY OTP LOGIN
@router.post("/verify-otp")
def verify_login_otp(data: VerifyRequest):

    return UserLoginService.verify_login(data.mobile_number, data.otp)
