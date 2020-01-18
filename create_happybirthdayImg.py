#!/usr/bin/env python
# encoding: utf-8
# @Time : 2020-01-17 10:24

__author__ = 'M'

from PIL import Image, ImageFont, ImageDraw
import os
import re

# 建立一个字典用来存放头图、标题、心形图片、诗句
content={
    "back_img":"pre/paper.jpg",
    "001":{
        "ad":'Happy Birthday',
        "ad2":'The love, is same with the coal, burns, must try to find solution,to call it to cool. Let it wilfully, that must scorch a heart',        
        "head":'001.jpg',
        "heart":'010.jpg'
    },
    "002": {
        "ad": 'To',
        "ad2":'It also is most wisdom crazy, chokes up the throat the bitter taste, can not eat the mouth the honey',        
        "head": '002.jpg',
        "heart":'010.jpg'
    },
    "003": {
        "ad": 'WW_Icecube',
        "ad2":'Likes liking a tug-of-war competition, as soon as to start, not to beable to stop',        
        "head": '003.jpg',
        "heart":'010.jpg'
    },
    "004": {
        "ad": 'January 30,1980',
        "ad2":'Liked letting the person change, clever suddenly starts gently, liked letting the person go bad, had understood, when should act shamelessly',        
        "head": '004.jpg',
        "heart":'010.jpg'
    },
    "005": {
        "ad": 'TO',
        "ad2":'The love, is same with the coal, burns, must try to find solutionto call it to cool. Let it wilfully, that must scorch a heart',        
        "head": '005.jpg',
        "heart":'010.jpg'
    },
    "006": {
        "ad": 'January 30,2020',
        "ad2":'So long as you clearly treasure, like with liking, I being willing to wait, for you will give my future',        
        "head": '006.jpg',
        "heart":'010.jpg'
    },
    "007": {
        "ad": 'LOVE',
        "ad2":'Your happy love, is a treasure, I disdain the situation, to exchange with the king',        
        "head": '007.jpg',
        "heart":'010.jpg'
    },
    "008": {
        "ad": 'YOU',
        "ad2":'The true love, is cannot, use the spoken language expression, the behavior is loyal best showing',        
        "head": '008.jpg',
        "heart":'010.jpg'
    },
    "009": {
        "ad": 'FOREVER',
        "ad2":'I feel your presence enter me,like the morning sun\'s early light,filling my memories and dreams of us,with a warm and clear radiance,You have become my love, my life',        
        "head": '009.jpg',
        "heart":'010.jpg'
    }
}


# 将所有获取到的字典元素按照需要的版式绘制在底图上
def get_pic(background,head,adcontent,adcontent2,heart,pic_name):

    im = Image.open(background) 

    head_img = Image.open(f"head/{head}").resize((600,595),Image.ANTIALIAS) # 处理头图
    im.paste(head_img,(0,0)) 
    draw = ImageDraw.Draw(im)

    head_img = Image.open(f"head/{heart}").resize((300,300),Image.ANTIALIAS) # 处理心形图片
    im.paste(head_img,(159,850))
    draw = ImageDraw.Draw(im)


    fnt = ImageFont.truetype("pre/odstemplikbold.ttf",90) # 摄制字体
   

    y_pos = 180 # 处理标题
    ad_w, ad_h = draw.textsize(adcontent, font=fnt)
    draw.text(((600 - ad_w) / 2, y_pos+600), adcontent, font=fnt,fill=(145, 0, 0))
    y_pos += ad_h + 10


    ad2_parts = re.split(r'[,.]', adcontent2) # 处理诗句
    y2_pos = 180
    fnt2 = ImageFont.truetype("pre/odstemplikbold.ttf",40)
    for ad2_part in ad2_parts:
        if ad2_part!=ad2_parts[-1]:
            ad2_w,ad2_h = draw.textsize(ad2_part+",", font=fnt2)
            draw.text(((600-ad2_w)/2,y2_pos+1050),ad2_part+",",font=fnt2,fill=(145,0,0))
            y2_pos +=ad_h-20
        else:
            ad2_w, ad2_h = draw.textsize(ad2_part, font=fnt2)
            draw.text(((600 - ad2_w) / 2, y2_pos+1050), ad2_part, font=fnt2, fill=(145,0,0))
            y2_pos += ad2_h - 20

    im.save(pic_name) # 保存图片
            

if __name__== "__main__":
    for i in range(1,10): # 循环获取字典的内容
        background = "pre/paper.jpg"
        head = content[f'00{i}']['head']
        heart = content[f'00{i}']['heart']
        adcontent = content[f'00{i}']['ad']
        adcontent2 = content[f'00{i}']['ad2']
        get_pic(background,head,adcontent,adcontent2,heart,f"{i}.jpg")
    print("九宫格图片生成完毕！")
    path='D:\\PythonLearning\\friends_ad_HappyBirthdayImg'# 调试程序使用，打开生成图片的目录
    os.system("start explorer %s" % path)

