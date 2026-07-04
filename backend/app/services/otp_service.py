import random
import time


class OTPService:

    otp_store = {} # temporary memory storage

    @staticmethod
    def generate_otp(mobile_number: str):

        otp = random.randint(100000, 999999)

        # store OTP with expiry (5 minutes)
        OTPService.otp_store[mobile_number] = {
            "otp": otp,
            "expiry": time.time() + 300
        }

        return otp

    @staticmethod
    def verify_otp(mobile_number: str, otp: int):

        if mobile_number not in OTPService.otp_store:
            return False

        stored_data = OTPService.otp_store[mobile_number]

        # check expiry
        if time.time() > stored_data["expiry"]:
            return False

        # check OTP match
        if stored_data["otp"] == otp:
            return True

        return False
