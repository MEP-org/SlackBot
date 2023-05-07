from fastapi import FastAPI
from SlackBot import SlackBot

app = FastAPI()
slack_bot = SlackBot()

@app.get("/")
async def root():
    return "Slack Bot for MepML is running!"


@app.post("/send_message")
async def send_message(channel: str, message: str):
    if slack_bot.post_message(channel, message):
        return {"message": "Message sent!"}
    return {"message": "Error sending message!"}
    