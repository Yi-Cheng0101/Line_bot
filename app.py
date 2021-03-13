import os
from datetime import datetime

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from linebot import LineBotApi

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
    #image_url = "https://i.imgur.com/eTldj2E.png?1"
    ##line_bot_api.push_message(to, ImageSendMessage(original_content_url=image_url, preview_image_url=image_url))
    
    if (get_message == 'Hi') or (get_message == '嗨') or (get_message == '你好') or (get_message == '嘿') or (get_message == 'hi'):
        reply_0 = TextSendMessage(text='很高興有這次的機會，來讓我好好介紹我自己吧')
        reply_1 = TextSendMessage(text='國立清華⼤學資訊工程學系四年級，為106學年大一不分系美術組入學，⼤二分流於資訊⼯程學系，從⼩在美術班的環境下長大，⾼中開始決定將美術為輔專心於學業上的學習，在⼤學入學時藉由學科的表現加上術科上的展現，獲得不分系美術組第⼀位入學，最後選擇熱愛的資訊工程領域學習。')                     
        reply_2 = TextSendMessage(text='努力修課的同時也不斷的嘗試自⼰的不同可能，除了在系上研究Kubenetes於AI + IoT、邊緣運算的畢業專題外，也與電機系教授嘗試AI於妝容辨識的跨領域專題研究。⼤三獲選進入資工系學⽣叢集競賽隊伍，於新加坡國家超級電腦中⼼主辦的HPC-AI Competition在眾多國際⼤學隊伍中榮獲亞軍，接續擔任學⽣教練及參賽隊員於德國及中國所舉辦的學生超級電腦競賽，課後之餘也繼續在清華藝集創作畫圖，舉辦個展及擔任助教。')
        reply_3 = TextSendMessage(text='生活 履歷 簡介 亦程的生活')
        message = StickerSendMessage(package_id='11537',sticker_id='52002739')
        line_bot_api.reply_message(event.reply_token, message)
        line_bot_api.push_message(to, reply_0)
        line_bot_api.push_message(to, reply_1)
        line_bot_api.push_message(to, reply_2)
        line_bot_api.push_message(to, reply_3)
        return 0 
      
    if get_message == '履歷':
        reply_0 = TextSendMessage(text='https://drive.google.com/file/d/1f5XW6uy9w6FpqUAKrL4nOBHoWCDS2gIn/view?usp=sharing')
        reply_1 = TextSendMessage(text='這是我的英文版履歷')
        image_url = "https://imgur.com/gallery/laNVnPu"
        line_bot_api.push_message(to, ImageSendMessage(original_content_url=image_url, preview_image_url=image_url))
        line_bot_api.push_message(to, reply_0)
        line_bot_api.push_message(to, reply_1)
        return 0
        
        
    if get_message == '簡介':
        #tt = 'https://p.facebook.com/csofficeNTHU/photos/a.1864273603844281/2782546688683630/?type=3&source=48&__tn__=EH-R'
        tt = 'https://yi-cheng0101.github.io/Yi-Cheng0101/'
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
                        image_url='https://i.imgur.com/zubdvFK.jpg',
                        action=PostbackTemplateAction(
                            label='清華藝集',
                            text='postback text2',
                            data='action=buy&itemid=2'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/zubdvFK.jpg',
                        action=PostbackTemplateAction(
                            label='生活',
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
    
    if event.message.text == "看看":
        message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
            thumbnail_image_url='https://yi-cheng0101.github.io/Yi-Cheng0101/images/IMG_0297.jpg',
            title='Menu',
            text='Please select',
            actions=[
                PostbackTemplateAction(
                    label='postback',
                    text='postback text',
                    data='action=buy&itemid=1'
                ),
                MessageTemplateAction(
                    label='message',
                    text='message text'
                ),
                URITemplateAction(
                    label='uri',
                    uri='https://yi-cheng0101.github.io/Yi-Cheng0101/posts/my-third-post/'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)
    
if __name__ == '__main__':
    app.run()

