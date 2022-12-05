import random
from datetime import date
from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event,Message,GroupMessageEvent,MessageSegment
import requests
import json
from nonebot.typing import T_State

def luck_simple(num):
    if num < 50:
        return 'hello'
    else:
        return 'world'
    

jrrp = on_keyword(['test'],priority=50)
@jrrp.handle()
async def jrrp_handle(bot: Bot, event: Event):
    rnd = random.Random()
    lucknum = rnd.randint(1,100)
    sound = f"file:///D:/Software/nonebot/Abiogenesis/src/plugins/image_send/sound.mp3" 
    await jrrp.send(MessageSegment.record(sound))
    await jrrp.finish(Message(f'[CQ:at,qq={event.get_user_id()}]{luck_simple(lucknum)}'))



from nonebot.rule import to_me

word=on_keyword({"你好"},rule=to_me())

@word.handle()
async def _(bot:Bot,event:GroupMessageEvent,state:T_State): 
    msg = await mc_img()
    await word.send(MessageSegment.at(event.user_id)+Message('你好哇'+msg))
async def mc_img():
    url = 'https://api.likepoems.com/img/sina/mc'
    pic = requests.get(url)
    pic_ti = f"[CQ:image,file={pic.url}]"
    return pic_ti