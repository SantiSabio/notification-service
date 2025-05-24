from pydantic import BaseModel, EmailStr

class Notification(BaseModel):
    event_type: str
    recipient : EmailStr
    message: str