from app.schemas.user import UserRegistration


class UserAuth:

    @staticmethod
    def register(user: UserRegistration):

        return {
            "success": True,
            "message": "User Registered Successfully",
            "user": {
                "full_name": user.full_name,
                "mobile_number": user.mobile_number,
                "role": user.role
            }
        }
