import nonebot
from nonebot import require
import requests
import urllib3
from nonebot.adapters.onebot.v11 import Bot, Event,Message,GroupMessageEvent,MessageSegment
# 设置一个定时器
timing = require("nonebot_plugin_apscheduler").scheduler
@timing.scheduled_job("cron", hour='8', minute = '05' , second = '00' ,id="dingshi")
async def morning():
    #这里是获取bot对象
    (bot,) = nonebot.get_bots().values()
    msg =  f"[CQ:tts,text='早上好 该起床了']" 
    sound = f"file:///D:/Software/nonebot/Abiogenesis/src/plugins/image_send/sound.mp3"
    await bot.send_msg(
        message_type="user",
        user_id=2422760965,
        message="早上好"+MessageSegment.record(sound)
    )
    
def tts_sound():
    content = " 早上好，该起床了"
    url = 'https://genshin.azurewebsites.net/api/speak?format=mp3&text=' + content +'&id=22'
    print(url)
    sound = requests.get(url)
    with open(content+'.mp3','wb') as file:
        file.write(sound.content)
    return url


'''
    with open(content+'.mp3','wb') as file:
        file.write(sound.content)
'''