import os
from datetime import datetime

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.environ.get("CHANNEL_SECRET"))


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
    #reply = TextSendMessage(text=f"{get_message}")
    #line_bot_api.reply_message(event.reply_token, url="http://web.cs.nthu.edu.tw/p/406-1174-193149,r109.php")
    message = ImageSendMessage(
    original_content_url='http://web.cs.nthu.edu.tw/var/file/174/1174/pictures/905/m/mczh-tw1280x800_large36424_319472822358.png',
    preview_image_url='http://web.cs.nthu.edu.tw/var/file/174/1174/pictures/905/m/mczh-tw1280x800_large36424_319472822358.png'
    )
    line_bot_api.reply_message(event.reply_token, message)
    #line_bot_api.reply_message(event.reply_token, reply)
