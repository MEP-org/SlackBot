import slack_sdk as slack
import os
from dotenv import load_dotenv
load_dotenv()

SLACK_TOKEN = os.environ.get("slack-token")

class SlackBot:

    def __init__(self):
        self.client = slack.WebClient(token=SLACK_TOKEN)

    def post_message(self, channel, message):
        try:
            self.client.chat_postMessage(
                channel=f"#{channel}",
                text=message
            )
            return True
        except Exception as e:
            print("Error posting message: ", e)
            return False
