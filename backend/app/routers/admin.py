from fastapi import APIRouter
from app.schemas.admin import AdminLogin

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

@router.post("/login")
def admin_login(admin: AdminLogin):
    if (
        admin.email == "admin@firstchoiceinfra.com"
        and admin.password == "Admin@123"
    ):
        return {
            "success": True,
            "message": "Admin Login Successful"
        }

    return {
        "success": False,
        "message": "Invalid Email or Password"
    }
