from pydantic import BaseModel
from typing import Literal


class UserRegistration(BaseModel):
    full_name: str
    mobile_number: str
    role: Literal["Buyer", "Owner", "Agent", "Builder"]
