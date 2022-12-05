from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message
from nonebot.plugin import on_keyword
import requests
import urllib3

def get_content():
	url = 'https://api.oick.cn/dog/api.php'
	get = requests.get(url).text
	return get
    

start = on_keyword(['舔狗日记'],priority=50)
@start.handle()
async def start_handle(bot: Bot, event: Event):
    await start.finish(Message(f'[CQ:at,qq={event.get_user_id()}]{get_content()}'))

test = on_keyword(['114514'],priority=50)
@test.handle()
async def test_handle(bot: Bot, event: Event):
    await test.finish(Message(f'[CQ:at,qq={event.get_user_id()}]{get_content()}'))