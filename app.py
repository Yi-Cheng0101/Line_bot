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
#t = 0

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
    
    if (get_message == 'Hi') or (get_message == '嗨') or (get_message == '你好') or (get_message == '嘿') or (get_message == 'hi') or (get_message == '簡介'):
        reply_0 = TextSendMessage(text='很高興有這次的機會，來讓我好好介紹我自己吧😆')
        reply_1 = TextSendMessage(text='個人簡介：      國立清華⼤學資訊工程學系四年級，為106學年大一不分系美術組入學，⼤二分流於資訊⼯程學系，從⼩在美術班的環境下長大，⾼中開始決定將美術為輔專心於學業上的學習，在⼤學入學時藉由學科的表現加上術科上的展現，獲得不分系美術組第⼀位入學，最後選擇熱愛的資訊工程領域學習。')                     
        reply_2 = TextSendMessage(text='學科表現🎓：    除了在系上研究Kubenetes於AI + IoT、邊緣運算的畢業專題外，也與電機系教授嘗試AI於妝容辨識的跨領域專題研究。⼤三獲選進入資工系學⽣叢集競賽隊伍👨‍💻，於新加坡國家超級電腦中⼼主辦的HPC-AI Competition在眾多國際⼤學隊伍中榮獲亞軍，接續擔任學⽣教練及參賽隊員於德國及中國所舉辦的學生超級電腦競賽。')
        reply_3 = TextSendMessage(text='術科表現🎨：    從小有美術班的背景，大學時於清華美術校隊[清華藝集]持續創作，在大二時擔任助教一職，協助整個藝集的運作，帶領大家參與藝術中心30週年活動與林正盛導演合作拍攝紀錄片、策展等，作品也獲通識教育中心展於教育學術論  壇於旺宏館大半圓，大三下時也在清華大學清大藝術工坊開設個人展覽。')
        reply_4 = TextSendMessage(text='看完我的簡介後，你可以打以下關鍵字！ 『簡介』『履歷』『大學時光』『生活』『外部連結』『程式作品』就可以看更多喔')
        
     
        message = StickerSendMessage(package_id='11537',sticker_id='52002739')
        line_bot_api.reply_message(event.reply_token, message)
        line_bot_api.push_message(to, reply_0)
        line_bot_api.push_message(to, reply_1)
        line_bot_api.push_message(to, reply_2)
        line_bot_api.push_message(to, reply_3)
        line_bot_api.push_message(to, reply_4)
        return 0 
      
    elif get_message == '履歷':
        
        #reply_0 = TextSendMessage(text='https://drive.google.com/file/d/1f5XW6uy9w6FpqUAKrL4nOBHoWCDS2gIn/view?usp=sharing')
        reply_1 = TextSendMessage(text='這是我的英文版履歷！')
        #reply_2 = TextSendMessage(text='更多學術研究在這喔!')
        image_url = "https://github.com/Yi-Cheng0101/Yi-Cheng0101/blob/main/public/images/fullsizeoutput_150f.jpeg?raw=true"
        
        message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
                text='看更多研究?',
                actions=[
                    URIAction(
                        label='Yes',
                        text='postback text',
                        data='action=buy&itemid=1',
                        uri='https://yi-cheng0101.github.io/Yi-Cheng0101/posts/my-second-post/'
                    ),
                    MessageTemplateAction(
                        label='No',
                        text='可以再輸入關鍵字更認識我，關鍵字！ 『簡介』『履歷』『大學時光』『生活』『外部連結』『程式作品』來認識我喔'
                    )
                ]
            )
        )
        
        
        line_bot_api.push_message(to, ImageSendMessage(original_content_url=image_url, preview_image_url=image_url))
        #line_bot_api.push_message(to, reply_0)
        line_bot_api.push_message(to, reply_1)
        #line_bot_api.push_message(to, reply_2)
        line_bot_api.push_message(to, message)
        #reply_f = TextSendMessage(text='關鍵字！ 『簡介』『履歷』『大學時光』『生活』『外部連結』『程式作品』來認識我喔')
        #response = line_bot_api.push_message(to, reply_f)
        return 0
        
        
    elif get_message == '程式作品':
        
        #tt = 'https://p.facebook.com/csofficeNTHU/photos/a.1864273603844281/2782546688683630/?type=3&source=48&__tn__=EH-R'
        tt = 'https://github.com/Yi-Cheng0101'
        reply = TextSendMessage(text=tt)
        line_bot_api.reply_message(event.reply_token, reply)
        reply_f = TextSendMessage(text='關鍵字！ 『簡介』『履歷』『大學時光』『生活』『外部連結』『程式作品』來認識我喔')
        response = line_bot_api.push_message(to, reply_f)
        return 0
    
    
    elif get_message == '生活':
        message = ImagemapSendMessage(
            base_url='https://github.com/Yi-Cheng0101/Yi-Cheng0101/blob/main/public/images/IMG_1822.JPG?raw=true',
            alt_text='this is an imagemap',
            base_size=BaseSize(height=1040, width=1040),
            actions=[
                MessageImagemapAction(
                    text='這是我們家，我們常常利用休息的假日到處走走 🚘',
                    area=ImagemapArea(
                        x=0, y=0, width=520, height=520
                    )
                ),
                MessageImagemapAction(
                    text='這是我出生的地方彰化社頭，農村的小鄉鎮 ☀',
                    area=ImagemapArea(
                        x=520, y=0, width=520, height=520
                    )
                ),
                MessageImagemapAction(
                    text='這是我教小朋友畫圖，寒暑假有空的話我常常會去小學教小朋友畫圖，這是去年我去台東鸞山國小時拍的 🗣',
                    area=ImagemapArea(
                        x=0, y=520, width=520, height=520
                    )
                ),
                MessageImagemapAction(
                    text='這是我平常想要放鬆時，都會喜歡跑去海邊，還可以讓我平靜又放鬆 🌊',
                    area=ImagemapArea(
                        x=520, y=520, width=520, height=520
                    )
                )  
            ]
            
        )
        reply = TextSendMessage(text='可以點圖片看我介紹我的生活！')
        line_bot_api.reply_message(event.reply_token, message)
        line_bot_api.push_message(to, reply)
        
    
    elif event.message.text == "大學時光":
       
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
    
    elif event.message.text == "部落格":
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
       
        
    elif event.message.text == "外部連結":
        message = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://github.com/Yi-Cheng0101/Yi-Cheng0101/blob/main/public/images/C72D0AA6-A225-4830-ADB6-0A082E76295E.jpg?raw=true',
                        title='Blog',
                        text='我的部落格',
                        actions=[
                            PostbackTemplateAction(
                                label='簡介',
                                text='特別為了這次ChatBot做的Blog',
                                data='action=buy&itemid=1'
                            ),
                            MessageTemplateAction(
                                label='內容',
                                text='裡面充滿了我的點滴喔'
                            ),
                            URITemplateAction(
                                label='連結',
                                uri='https://yi-cheng0101.github.io/Yi-Cheng0101/'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://scontent.ftpe3-2.fna.fbcdn.net/v/t1.0-9/126284594_2782546692016963_574399515281676441_o.jpg?_nc_cat=102&ccb=1-3&_nc_sid=730e14&_nc_ohc=YOTPLfg9gM4AX9Medmz&_nc_ht=scontent.ftpe3-2.fna&oh=91d2cf3f9a3902c82e70bb12cda8fc5e&oe=607358CA',
                        title='2020 APAC Seconfd Prize',
                        text='系上報導',
                        actions=[
                            PostbackTemplateAction(
                                label='簡介',
                                text='恭賀拿到亞軍',
                                data='action=buy&itemid=1'
                            ),
                            MessageTemplateAction(
                                label='內容',
                                text='賀!資工系王子文等7位同學榮獲2020 APAC HPC-AI Competition Second Prize (指導教授:周志遠教授)'
                            ),
                            URITemplateAction(
                                label='連結',
                                uri='https://www.facebook.com/csofficeNTHU/photos/a.1864273603844281/2782546688683630'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://scontent-hkt1-1.xx.fbcdn.net/v/t1.0-9/p960x960/95332948_1860075580795900_3815032265772105728_o.jpg?_nc_cat=101&ccb=1-3&_nc_sid=730e14&_nc_ohc=9EfbUbtvBmIAX-eYNuX&_nc_ht=scontent-hkt1-1.xx&tp=6&oh=6a42570432aa597212df9fac7fbc3ab9&oe=60762F72',
                        title='一覺自然醒過來 蕭亦程 個展',
                        text='清大藝術中心報導',
                        actions=[
                            PostbackTemplateAction(
                                label='簡介',
                                text='【一覺自然醒過來｜2020蕭亦程個展】',
                                data='action=buy&itemid=1'
                            ),
                            MessageTemplateAction(
                                label='內容',
                                text='上大學以後，畫圖變成蕭亦程記錄生活的方式，「一覺自然醒過來」記錄著他從申請大學時的作品集到現在的創作，呈現他對自我的探索。'
                            ),
                            URITemplateAction(
                                label='連結',
                                uri='https://www.facebook.com/nthuarts/posts/1860206264116165/'
                            )
                        ]
                    )
                 ]
            )
           
        )
        line_bot_api.reply_message(event.reply_token, message)
        reply_f = TextSendMessage(text='關鍵字！ 『簡介』『履歷』『大學時光』『生活』『外部連結』『程式作品』來認識我喔')
        response = line_bot_api.push_message(to, reply_f)
    
        


    
if __name__ == '__main__':
    app.run()

