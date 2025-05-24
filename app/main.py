from fastapi import FastAPI
from app.models import Notification

app= FastAPI()

@app.get("/")
def read_root():
    return{"message": "Notification service is running!"}

@app.post("/notify")
def notify(notification: Notification):
    print("Encolando mensaje:", notification.dict())
    return {"status": "Message received", "data": notification.dict()}
