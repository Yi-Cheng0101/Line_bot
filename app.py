import os
from datetime import datetime

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

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
    
    # get user id when reply
    user_id = event.source.user_id
    to = user_id
    print("user_id =", user_id)
    image_url = "https://i.imgur.com/eTldj2E.png?1"
    line_bot_api.push_message(to, ImageSendMessage(original_content_url=image_url, preview_image_url=image_url))
    
    if get_message == 'Hi':
        reply = TextSendMessage(text='我想睡覺')
        message = StickerSendMessage(package_id='1',sticker_id='1')
        line_bot_api.reply_message(event.reply_token, message)
        line_bot_api.reply_message(event.reply_token, reply)
        return 0 
      
    if get_message == '簡介':
        tt = 'https://p.facebook.com/csofficeNTHU/photos/a.1864273603844281/2782546688683630/?type=3&source=48&__tn__=EH-R'
        reply = TextSendMessage(text=tt)
        line_bot_api.reply_message(event.reply_token, reply)
        return 0
    
    
    if get_message == '亦程的生活':
        message = ImagemapSendMessage(
            base_url='https://i.imgur.com/zubdvFK.jpg',
            alt_text='this is an imagemap',
            base_size=BaseSize(height=1040, width=1040),
            actions=[
                URIImagemapAction(
                    link_uri='https://i.imgur.com/zubdvFK.jpg',
                    area=ImagemapArea(
                        x=0, y=0, width=520, height=1040
                    )
                ),
                MessageImagemapAction(
                    text='hello',
                    area=ImagemapArea(
                        x=520, y=0, width=520, height=1040
                    )
                )
            ]
        )
        line_bot_api.reply_message(event.reply_token, message)
    
    
    if event.message.text == "生活":
        message = TemplateSendMessage(
            alt_text='ImageCarousel template',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://imgur.com/gallery/jJhv5Z6.jpg',
                        action=PostbackTemplateAction(
                            label='postback1',
                            text='postback text1',
                            data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/zubdvFK.jpg',
                        action=PostbackTemplateAction(
                            label='postback2',
                            text='postback text2',
                            data='action=buy&itemid=2'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/zubdvFK.jpg',
                        action=PostbackTemplateAction(
                            label='postback2',
                            text='postback text2',
                            data='action=buy&itemid=2'
                        )
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        #reply = TextSendMessage(text='這是我的生活')
        #Channel.find_or_create_by(channel_id: channel_id)
        #response = line.push_message(channel_id, replay)
        return 0
    
if __name__ == '__main__':
    app.run()

