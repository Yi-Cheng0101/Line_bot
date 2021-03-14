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
        reply_0 = TextSendMessage(text='很高興有這次的機會，來讓我好好介紹我自己吧😆')
        reply_1 = TextSendMessage(text='個人簡介：      國立清華⼤學資訊工程學系四年級，為106學年大一不分系美術組入學，⼤二分流於資訊⼯程學系，從⼩在美術班的環境下長大，⾼中開始決定將美術為輔專心於學業上的學習，在⼤學入學時藉由學科的表現加上術科上的展現，獲得不分系美術組第⼀位入學，最後選擇熱愛的資訊工程領域學習。')                     
        reply_2 = TextSendMessage(text='學科表現🎓：    除了在系上研究Kubenetes於AI + IoT、邊緣運算的畢業專題外，也與電機系教授嘗試AI於妝容辨識的跨領域專題研究。⼤三獲選進入資工系學⽣叢集競賽隊伍👨‍💻，於新加坡國家超級電腦中⼼主辦的HPC-AI Competition在眾多國際⼤學隊伍中榮獲亞軍，接續擔任學⽣教練及參賽隊員於德國及中國所舉辦的學生超級電腦競賽。')
        reply_3 = TextSendMessage(text='術科表現🎨：    從小有美術班的背景，大學時於清華美術校隊[清華藝集]持續創作，在大二時擔任助教一職，協助整個藝集的運作，帶領大家參與藝術中心30週年活動與林正盛導演合作拍攝紀錄片、策展等，作品也獲通識教育中心展於教育學術論  壇於旺宏館大半圓，大三下時也在清華大學清大藝術工坊開設個人展覽。')
        reply_4 = TextSendMessage(text='看完我的簡介後，你可以打以下關鍵字！ 『履歷』『亦程的大學生活』就可以看更多喔')
        
     
        message = StickerSendMessage(package_id='11537',sticker_id='52002739')
        line_bot_api.reply_message(event.reply_token, message)
        line_bot_api.push_message(to, reply_0)
        line_bot_api.push_message(to, reply_1)
        line_bot_api.push_message(to, reply_2)
        line_bot_api.push_message(to, reply_3)
        line_bot_api.push_message(to, reply_4)
        return 0 
      
    if get_message == '履歷':
        reply_0 = TextSendMessage(text='https://drive.google.com/file/d/1f5XW6uy9w6FpqUAKrL4nOBHoWCDS2gIn/view?usp=sharing')
        reply_1 = TextSendMessage(text='這是我的英文版履歷！')
        reply_2 = TextSendMessage(text='更多學術研究在這喔!')
        image_url = "https://github.com/Yi-Cheng0101/Yi-Cheng0101/blob/main/public/images/fullsizeoutput_150f.jpeg?raw=true"
        
        message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
                text='Are you sure?',
                actions=[
                    URIAction(
                        label='Yes',
                        text='postback text',
                        data='action=buy&itemid=1',
                        uri='https://yi-cheng0101.github.io/Yi-Cheng0101/posts/my-second-post/'
                    ),
                    MessageTemplateAction(
                        label='message',
                        text='message text'
                    )
                ]
            )
        )

        
        line_bot_api.push_message(to, ImageSendMessage(original_content_url=image_url, preview_image_url=image_url))
        line_bot_api.push_message(to, reply_0)
        line_bot_api.push_message(to, reply_1)
        line_bot_api.push_message(to, reply_2)
        line_bot_api.push_message(to, message)
        return 0
        
        
    if get_message == '簡介':
        #tt = 'https://p.facebook.com/csofficeNTHU/photos/a.1864273603844281/2782546688683630/?type=3&source=48&__tn__=EH-R'
        tt = 'https://yi-cheng0101.github.io/Yi-Cheng0101/'
        reply = TextSendMessage(text=tt)
        line_bot_api.reply_message(event.reply_token, reply)
        return 0
    
    
    if get_message == '亦程的生活':
        message = ImagemapSendMessage(
            base_url='https://github.com/Yi-Cheng0101/Yi-Cheng0101/blob/main/public/images/IMG_1822.JPG?raw=true',
            alt_text='this is an imagemap',
            base_size=BaseSize(height=1040, width=1040),
            actions=[
                MessageImagemapAction(
                    text='當我很累想放鬆時，最常去海邊',
                    area=ImagemapArea(
                        x=0, y=0, width=520, height=520
                    )
                ),
                MessageImagemapAction(
                    text='我教小朋友畫圖',
                    area=ImagemapArea(
                        x=520, y=0, width=520, height=520
                    )
                ),
                MessageImagemapAction(
                    text='我運動',
                    area=ImagemapArea(
                        x=0, y=520, width=520, height=520
                    )
                ),
                MessageImagemapAction(
                    text='我的家',
                    area=ImagemapArea(
                        x=520, y=520, width=520, height=520
                    )
                )  
            ]
            
        )
        line_bot_api.reply_message(event.reply_token, message)
    
    
    if event.message.text == "亦程的大學生活":
        message = TemplateSendMessage(
            alt_text='ImageCarousel template',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://raw.githubusercontent.com/Yi-Cheng0101/Yi-Cheng0101/main/public/images/IMG_0297.jpg',
                        #action=PostbackTemplateAction(
                        action=URIAction(
                            label='學生叢集競賽',
                            text='postback text2',
                            data='action=buy&itemid=2',
                            uri='https://yi-cheng0101.github.io/Yi-Cheng0101/posts/my-third-post/'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://yi-cheng0101.github.io/Yi-Cheng0101/images/D8CAB960-A067-4497-AC8A-C13313BC59D5.JPG',
                        action=URIAction(
                            label='專題研究',
                            text='postback text2',
                            data='action=buy&itemid=2',
                            uri='https://yi-cheng0101.github.io/Yi-Cheng0101/posts/my-second-post/'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://yi-cheng0101.github.io/Yi-Cheng0101/images/IMG_1800.JPG',
                        action=URIAction(
                            label='清華藝集',
                            text='postback text2',
                            data='action=buy&itemid=2',
                            uri='https://yi-cheng0101.github.io/Yi-Cheng0101/posts/my-first-post/'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://github.com/Yi-Cheng0101/Yi-Cheng0101/blob/main/public/images/2360A9C0-F546-444B-9CAC-BE1382AA286E.JPG?raw=true',
                        action=URIAction(
                            label='生活',
                            text='postback text2',
                            data='action=buy&itemid=2',
                            uri='https://yi-cheng0101.github.io/Yi-Cheng0101/posts/my-fourth-post/'
                        )
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        reply = TextSendMessage(text='可以點進去看更多')
        response = line_bot_api.push_message(to, reply)
        return 0
    
    if event.message.text == "亦程的部落格":
        message = TemplateSendMessage(
            alt_text='Buttons template',
                template=ButtonsTemplate(
                thumbnail_image_url='https://github.com/Yi-Cheng0101/Yi-Cheng0101/blob/main/public/images/fullsizeoutput_1511.jpeg?raw=true',
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
                        uri='https://yi-cheng0101.github.io/Yi-Cheng0101/'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    
    if event.message.text == "外部連結":
        message = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://github.com/Yi-Cheng0101/Yi-Cheng0101/blob/main/public/images/fullsizeoutput_1511.jpeg?raw=true',
                        title='this is menu1',
                        text='description1',
                        actions=[
                            PostbackTemplateAction(
                                label='postback1',
                                text='postback text1',
                                data='action=buy&itemid=1'
                            ),
                            MessageTemplateAction(
                                label='message1',
                                text='message text1'
                            ),
                            URITemplateAction(
                                label='uri1',
                                uri='https://yi-cheng0101.github.io/Yi-Cheng0101/'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='data:image/jpeg;base64,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',
                        title='this is menu2',
                        text='description2',
                        actions=[
                            PostbackTemplateAction(
                                label='postback2',
                                text='postback text2',
                                data='action=buy&itemid=2'
                            ),
                            MessageTemplateAction(
                                label='message2',
                                text='message text2'
                            ),
                            URITemplateAction(
                                label='uri2',
                                uri='https://p.facebook.com/csofficeNTHU/photos/a.1864273603844281/2782546688683630/?type=3&source=48&__tn__=EH-R'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    
if __name__ == '__main__':
    app.run()

