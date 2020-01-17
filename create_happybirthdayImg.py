#!/usr/bin/env python
# encoding: utf-8
# @Time : 2020-01-17 10:24

__author__ = 'M'

from PIL import Image, ImageFont, ImageDraw

content={
    "back_img":"pre/paper.jpg",
    "001":{
        "ad":'Happy Birthday',
        "head":'001.jpg',
        "heart":'010.jpg'
    },
    "002": {
        "ad": 'To',
        "head": '002.jpg',
        "heart":'010.jpg'
    },
    "003": {
        "ad": 'WW_Icecube',
        "head": '003.jpg',
        "heart":'010.jpg'
    },
    "004": {
        "ad": 'January 30,1980',
        "head": '004.jpg',
        "heart":'010.jpg'
    },
    "005": {
        "ad": 'TO',
        "head": '005.jpg',
        "heart":'010.jpg'
    },
    "006": {
        "ad": 'January 30,2020',
        "head": '006.jpg',
        "heart":'010.jpg'
    },
    "007": {
        "ad": 'LOVE',
        "head": '007.jpg',
        "heart":'010.jpg'
    },
    "008": {
        "ad": 'YOU',
        "head": '008.jpg',
        "heart":'010.jpg'
    },
    "009": {
        "ad": 'FOREVER',
        "head": '009.jpg',
        "heart":'010.jpg'
    }
}
def get_pic(background,head,adcontent,heart,pic_name):
    im = Image.open(background)

    head_img = Image.open(f"head/{head}").resize((600,595),Image.ANTIALIAS)
    im.paste(head_img,(0,0))
    draw = ImageDraw.Draw(im)

    head_img = Image.open(f"head/{heart}").resize((300,300),Image.ANTIALIAS)
    im.paste(head_img,(159,800))
    draw = ImageDraw.Draw(im)

    fnt = ImageFont.truetype("pre/odstemplikbold.ttf",90)

    y_pos = 180
    ad_w, ad_h = draw.textsize(adcontent, font=fnt)
    draw.text(((600 - ad_w) / 2, y_pos+550), adcontent, font=fnt,fill=(255, 0, 0))
    y_pos += ad_h + 10
    im.save(pic_name)

if __name__== "__main__":
    for i in range(1,10):
        background = "pre/paper.jpg"
        head = content[f'00{i}']['head']
        heart = content[f'00{i}']['heart']
        adcontent = content[f'00{i}']['ad']
        get_pic(background,head,adcontent,heart,f"{i}.jpg")
    print("九宫格图片生成完毕！")

