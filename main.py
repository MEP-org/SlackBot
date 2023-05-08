from fastapi import FastAPI
from SlackBot import SlackBot
from pydantic import BaseModel

app = FastAPI()
slack_bot = SlackBot()

class Notification(BaseModel):
    channel: str
    message: str

@app.get("/")
async def root():
    return "Slack Bot for MepML is running!"


@app.post("/notify")
async def send_message(notification: Notification):
    if slack_bot.post_message(notification.channel, notification.message):
        return {"message": "Message sent!"}
    return {"message": "Error sending message!"}
    