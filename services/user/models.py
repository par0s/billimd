from pydantic import BaseModel
from datetime import datetime


class UserUpdateRequest(BaseModel):
    """
    Payload of user update request
    """
    user_id: str
    first_name: str
    password: str
    updated_datetime: datetime