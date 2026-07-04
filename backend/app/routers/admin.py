from fastapi import APIRouter
from app.schemas.admin import AdminLogin
from app.auth.admin_login import AdminAuth

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.post("/login")
def admin_login(admin: AdminLogin):
    return AdminAuth.login(admin)
