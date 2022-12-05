import cv2
import pytz
import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import datetime

from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import PrivateMessageEvent,Bot,Message,MessageSegment,Event

def makepic():
    phone = '13855135009'
    name = '高爽'
    phone = phone[:3] + "****" + phone[-4:]

    # 安康
    img = cv2.imread("D:\\Software\\nonebot\\Abiogenesis\\src\\plugins\\today_school\\akm.jpg")
    im1 = Image.new("RGB", (500, 60), (254, 254, 254))
    dr1 = ImageDraw.Draw(im1)
    dr1.text((0, 0), datetime.datetime.now(
            tz=pytz.timezone('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S"), (0, 0, 0),
             ImageFont.truetype("D:\\Software\\nonebot\\Abiogenesis\\src\\plugins\\today_school\\Medium.otf", 48))
    img[375: 435, 218: 718, :] = cv2.resize(np.array(im1), (500, 60))

    im2 = Image.new("RGB", (90, 50), (254, 254, 254))
    dr2 = ImageDraw.Draw(im2)
    dr2.text((0, 0), name, (0, 0, 0), ImageFont.truetype("D:\\Software\\nonebot\\Abiogenesis\\src\\plugins\\today_school\\Medium.otf", 36))
    img[275: 325, 110: 200, :] = cv2.resize(np.array(im2), (90, 50))
    cv2.imwrite("D:\\Software\\nonebot\\Abiogenesis\\src\\plugins\\today_school\\akm.jpg", img)

    # 行程
    img = cv2.imread("D:\\Software\\nonebot\\Abiogenesis\\src\\plugins\\today_school\\xck.jpg")
    im1 = Image.new("RGB", (176, 23), (254, 254, 254))
    dr1 = ImageDraw.Draw(im1)
    dr1.text((0, 0), datetime.datetime.now(
            tz=pytz.timezone('Asia/Shanghai')).strftime("%Y.%m.%d %H:%M:%S"), (120, 120, 120),
             ImageFont.truetype("D:\\Software\\nonebot\\Abiogenesis\\src\\plugins\\today_school\\Medium.otf", 18))
    img[235: 258, 135: 311, :] = cv2.resize(np.array(im1), (176, 23))

    im2 = Image.new("RGB", (200, 30), (254, 254, 254))
    dr2 = ImageDraw.Draw(im2)
    dr2.text((0, 0), phone + "的动态行程卡", (0, 0, 0), ImageFont.truetype("D:\\Software\\nonebot\\Abiogenesis\\src\\plugins\\today_school\\Medium.otf", 16))#注意字体文件用绝对路径
    img[200: 230, 85: 285, :] = cv2.resize(np.array(im2), (200, 30))
    cv2.imwrite("D:\\Software\\nonebot\\Abiogenesis\\src\\plugins\\today_school\\xck.jpg", img)

    return 0

    #核酸
    # pic_ti = f"[CQ:image,file={url}]"

#QQ发送
getjpg=on_keyword(['报备'],priority=50)
@getjpg.handle()

async def sendjpg(bot:Bot,event:PrivateMessageEvent,state:T_State):
    makepic()

    url1 = f"file:///D:/Software/nonebot/Abiogenesis/src/plugins/today_school/akm.jpg"
    url2 = f"file:///D:/Software/nonebot/Abiogenesis/src/plugins/today_school/xck.jpg"
    msg1 = f"[CQ:image,file={url1}]"
    msg2 = f"[CQ:image,file={url2}]"
    try:
        await getjpg.send(Message(msg1))
        await getjpg.send(Message(msg2))
    except CQHttpError:
        await getjpg.send(Message("error"))


def makepic_others():
    phone = '13855135009'
    name = '梁利彦'
    phone = phone[:3] + "****" + phone[-4:]

    # 安康
    img = cv2.imread("D:\\Software\\nonebot\\Abiogenesis\\src\\plugins\\today_school\\image\\akm.jpg")
    im1 = Image.new("RGB", (500, 60), (254, 254, 254))
    dr1 = ImageDraw.Draw(im1)
    dr1.text((0, 0), datetime.datetime.now(
            tz=pytz.timezone('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S"), (0, 0, 0),
             ImageFont.truetype("D:\\Software\\nonebot\\Abiogenesis\\src\\plugins\\today_school\\Medium.otf", 48))
    img[375: 435, 218: 718, :] = cv2.resize(np.array(im1), (500, 60))

    im2 = Image.new("RGB", (90, 50), (254, 254, 254))
    dr2 = ImageDraw.Draw(im2)
    dr2.text((0, 0), name, (0, 0, 0), ImageFont.truetype("D:\\Software\\nonebot\\Abiogenesis\\src\\plugins\\today_school\\Medium.otf", 30))
    img[280: 330, 90: 180, :] = cv2.resize(np.array(im2), (90, 50))
    cv2.imwrite("D:\\Software\\nonebot\\Abiogenesis\\src\\plugins\\today_school\\image\\akm.jpg", img)

    # 行程
    img = cv2.imread("D:\\Software\\nonebot\\Abiogenesis\\src\\plugins\\today_school\\image\\xck.jpg")
    im1 = Image.new("RGB", (176, 23), (254, 254, 254))
    dr1 = ImageDraw.Draw(im1)
    dr1.text((0, 0), datetime.datetime.now(
            tz=pytz.timezone('Asia/Shanghai')).strftime("%Y.%m.%d %H:%M:%S"), (120, 120, 120),
             ImageFont.truetype("D:\\Software\\nonebot\\Abiogenesis\\src\\plugins\\today_school\\Medium.otf", 18))
    img[235: 258, 135: 311, :] = cv2.resize(np.array(im1), (176, 23))

    im2 = Image.new("RGB", (200, 30), (254, 254, 254))
    dr2 = ImageDraw.Draw(im2)
    dr2.text((0, 0), phone + "的动态行程卡", (0, 0, 0), ImageFont.truetype("D:\\Software\\nonebot\\Abiogenesis\\src\\plugins\\today_school\\Medium.otf", 16))#注意字体文件用绝对路径
    img[200: 230, 85: 285, :] = cv2.resize(np.array(im2), (200, 30))
    cv2.imwrite("D:\\Software\\nonebot\\Abiogenesis\\src\\plugins\\today_school\\image\\xck.jpg", img)

    return 0

    #核酸
    # pic_ti = f"[CQ:image,file={url}]"

getjpg_others=on_keyword(['梁利彦'],priority=50)
@getjpg_others.handle()

async def sendjpg(bot:Bot,event:PrivateMessageEvent,state:T_State):
    makepic_others()

    url1 = f"file:///D:/Software/nonebot/Abiogenesis/src/plugins/today_school/image/akm.jpg"
    url2 = f"file:///D:/Software/nonebot/Abiogenesis/src/plugins/today_school/image/xck.jpg"
    msg1 = f"[CQ:image,file={url1}]"
    msg2 = f"[CQ:image,file={url2}]"
    try:
        await getjpg_others.send(Message(msg1))
        await getjpg_others.send(Message(msg2))
    except CQHttpError:
        await getjpg_others.send(Message("error"))

makepic_others()