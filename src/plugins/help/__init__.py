from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event, Bot
from random import randint
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import Event, Bot

help = on_command('help', aliases={'帮助'},priority=1)
@help.handle()
async def help_send(bot: Bot, event: Event):
    await help.finish(Message(
f'[CQ:at,qq={event.get_user_id()}]目前可接收的消息如下(输入命令+编号，可查看相关格式):\n\
1.random/随机数\n\
2.jrrp/今日人品\n\
3.kw+键+值  生成一个回复消息\n\
4.根据上面3生成的内容,发送对应键,即可回复\n\
5.随机图片(包括美图和涩图两种模式)\n\
6.一次发送5张一下的涩图\
'))
