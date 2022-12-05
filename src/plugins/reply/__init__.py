import random
from datetime import date
from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message


def luck_simple():
    rnd = random.Random()
    answer = [
                '既然你这么想，那么我也没办法',
                '啊对对对对',
                '既然你这么说，那么我也没办法',
                '随便你',
                '都行',
                '你看待问题的方式真有意思',
                '你真厉害',
                '哦，我知道了，还有别的事情吗',
                '我太不清楚原因，你自己问问吧',
                '你说得对',
                '确实',
                '那就这样吧',
                '挺好的啊',
                '你说的都对',
                '这方面不知道，不好说',
                '说再多也没用'
            ]

    num = rnd.randint(0,len(answer)-1)
    return answer[num]
    

jrrp = on_keyword(['帮我说句话','你怎么看'],priority=50)
@jrrp.handle()
async def jrrp_handle(bot: Bot, event: Event):
    
    await jrrp.finish(Message(f'[CQ:at,qq={event.get_user_id()}]{luck_simple()}'))