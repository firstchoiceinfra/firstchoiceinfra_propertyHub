from app.services.otp_service import OTPService
from app.schemas.user import UserRegistration


class UserLoginService:

    @staticmethod
    def login_with_otp(mobile_number: str):

        otp = OTPService.generate_otp(mobile_number)

        return {
            "success": True,
            "message": "OTP sent for login",
            "otp": otp # demo only
        }

    @staticmethod
    def verify_login(mobile_number: str, otp: int):

        result = OTPService.verify_otp(mobile_number, otp)

        if result:
            return {
                "success": True,
                "message": "Login successful"
            }

        return {
            "success": False,
            "message": "Invalid OTP"
        }
