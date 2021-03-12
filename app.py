import os
from datetime import datetime

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get("9cXJht4q7WSduoh1eLBpkh+KKfVGYQDxJO0M73yQsyYHZuwECrn57YEEiV3N/TRxxqxI/uPVjNMAl9ByoQmvrZgVkX3c7cBvh+4OJM8t+y0OHY2YPX7i7eBkBFeXoQjLSl0vl46aquYGXvy41h29PQdB04t89/1O/w1cDnyilFU="))
handler = WebhookHandler(os.environ.get("4818ef2864e2fefac2de9b5de6d1eb95"))


@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    get_message = event.message.text

    # Send To Line
    reply = TextSendMessage(text=f"{get_message}")
    line_bot_api.reply_message(event.reply_token, reply)
