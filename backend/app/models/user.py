from pydantic import BaseModel
from typing import Literal


class User(BaseModel):
    full_name: str
    mobile_number: str
    role: Literal["Buyer", "Owner", "Agent", "Builder"]
