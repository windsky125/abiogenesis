
from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,PrivateMessageEvent,Bot,Message,MessageSegment,Event
import requests
import json
#随机图片 
pic=on_keyword(['二次元图'],priority=50)
@pic.handle()
async def _(bot:Bot,event:Event,state:T_State):
    msg = await suijitu()
    try:
        await pic.send(Message(msg))
    except CQHttpError:
        await pic.send(Message("error"))
async def suijitu():
    #url='https://api.ghser.com/random/api.php'#'https://api.lolicon.app/setu/v2'
    url='https://api.yimian.xyz/img'
    pic = requests.get(url)
    pic_ti = f"[CQ:image,file={pic.url}]"
    return pic_ti
#p站图片
pixiv=on_keyword({'pixiv','p站图'})
@pixiv.handle()
async def start_pixiv(bot:Bot,event:Event,state:T_State):
    msg = await pivix_img()
    try:
        await pixiv.send(Message(msg))
    except CQHttpError:
        await pixiv.send(Message("error"))
async def pivix_img():
    url = 'https://api.likepoems.com/img/sina/pixiv'
    pic = requests.get(url)
    pic_ti = f"[CQ:image,file={pic.url}]"
    return pic_ti
#风景图片
nature=on_keyword({'风景图'})
@nature.handle()
async def start_pixiv(bot:Bot,event:Event,state:T_State):
    msg = await nature_img()
    try:
        await nature.send(Message(msg))
    except CQHttpError:
        await nature.send(Message("error"))
async def nature_img():
    url = 'https://api.likepoems.com/img/sina/nature'
    pic = requests.get(url)
    pic_ti = f"[CQ:image,file={pic.url}]"
    return pic_ti
#mc图
mc=on_keyword({'mc'})
@mc.handle()
async def start_pixiv(bot:Bot,event:Event,state:T_State):
    msg = await mc_img()
    try:
        await mc.send(Message(msg))
    except CQHttpError:
        await mc.send(Message("error"))
async def mc_img():
    url = 'https://api.likepoems.com/img/sina/mc'
    pic = requests.get(url)
    pic_ti = f"[CQ:image,file={pic.url}]"
    return pic_ti
#色图
anime_jpg=on_keyword({'来张色图','无内鬼'})
@anime_jpg.handle()
async def start_pixiv(bot:Bot,event:Event,state:T_State):
    msg = await anime_jpg_img()
    try:
        await anime_jpg.send(Message(msg))
    except CQHttpError:
        await anime_jpg.send(Message("error"))
async def anime_jpg_img():
    url = 'https://api.lolicon.app/setu/v2?size=regular'
    pic = requests.get(url)
    content = json.loads(pic.text)
    a = content['data']

    pic_ti = f"[CQ:image,file={a[-1]['urls']['regular']}]"
    return pic_ti
#r18
anime_jpg_r18=on_keyword({'r18'})
@anime_jpg_r18.handle()
async def start_pixiv(bot:Bot,event:PrivateMessageEvent,state:T_State):
    msg = await anime_jpg_img_r18()
    try:
        await anime_jpg_r18.send(Message(msg))
    except CQHttpError:
        await anime_jpg_r18.send(Message("error"))
async def anime_jpg_img_r18():
    url = 'https://api.lolicon.app/setu/v2?size=regular&r18=1'
    pic = requests.get(url)
    content = json.loads(pic.text)
    a = content['data']

    pic_ti = f"[CQ:image,file={a[-1]['urls']['regular']}]"
    return pic_ti
#腿控
anime_jpg_stockings=on_keyword({'丝袜','看看腿子'})
@anime_jpg_stockings.handle()
async def start_pixiv(bot:Bot,event:Event,state:T_State):
    msg = await anime_jpg_img_stockings()
    try:
        await anime_jpg_stockings.send(Message(msg))
    except CQHttpError:
        await anime_jpg_stockings.send(Message("error"))
async def anime_jpg_img_stockings():
    url = 'https://api.lolicon.app/setu/v2?size=regular&tag=白丝|黑丝'
    pic = requests.get(url)
    content = json.loads(pic.text)
    a = content['data']

    pic_ti = f"[CQ:image,file={a[-1]['urls']['regular']}]"
    return pic_ti
#
control=on_keyword({'来点色图'})
@control.handle()
async def start_control(bot:Bot,event:Event,state:T_State):
    url = f"file:///D:/Software/nonebot/Abiogenesis/src/plugins/image_send/1.png"
    msg1 = f"[CQ:image,file={url}]"
    msg = MessageSegment.at(event.user_id)+Message('年轻人要有节制')+Message(msg1)
    try:
        await control.send(Message(msg))
    except CQHttpError:
        await control.send(Message("error"))