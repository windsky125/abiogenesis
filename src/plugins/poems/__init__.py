from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.message import Message
from nonebot.plugin import on_keyword
import requests
import urllib3
import json


def get_content():
	url = 'https://v1.jinrishici.com/all'
	get = requests.get(url)
	data = json.loads(get.text)
	content = data['content'] + '\n《'+data['origin'] + '》\n'+data['author']

	return content
start = on_keyword(['诗词'],priority=50)
@start.handle()
async def start_handle(bot: Bot, event: Event):
    await start.finish(Message(f'[CQ:at,qq={event.get_user_id()}]{get_content()}'))

