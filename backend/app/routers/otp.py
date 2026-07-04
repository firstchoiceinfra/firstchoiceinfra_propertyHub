from fastapi import APIRouter
from pydantic import BaseModel

from app.services.otp_service import OTPService

router = APIRouter(
    prefix="/otp",
    tags=["OTP"]
)


# Request Model
class OTPRequest(BaseModel):
    mobile_number: str


class OTPVerifyRequest(BaseModel):
    mobile_number: str
    otp: int


# SEND OTP
@router.post("/send")
def send_otp(data: OTPRequest):

    otp = OTPService.generate_otp(data.mobile_number)

    return {
        "success": True,
        "message": "OTP sent successfully (demo)",
        "otp": otp # ⚠️ demo only
    }


# VERIFY OTP
@router.post("/verify")
def verify_otp(data: OTPVerifyRequest):

    result = OTPService.verify_otp(data.mobile_number, data.otp)

    if result:
        return {
            "success": True,
            "message": "OTP verified successfully"
        }

    return {
        "success": False,
        "message": "Invalid OTP or expired"
    }
