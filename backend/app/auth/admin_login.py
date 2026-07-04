from app.schemas.admin import AdminLogin


class AdminAuth:

    @staticmethod
    def login(admin: AdminLogin):

        if (
            admin.email == "admin@firstchoiceinfra.com"
            and admin.password == "Admin@123"
        ):

            return {
                "success": True,
                "message": "Login Successful",
                "role": "Admin"
            }

        return {
            "success": False,
            "message": "Invalid Email or Password"
        }
