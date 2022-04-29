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
'目前可接收的消息如下:\n\
1.random/随机数 \n@我使用该命令生成一个指定范围的随机数,\
如\'random 1 10 2\',其中\'1\'为随机数下线,10为随机数上限\n\n\
2.\'/jrrp\'或者\'/今日人品\'(\'/\'不能省略)\n生成你的运势数\n\n\
3.kw+键+值 \n生成一个回复消息 如\'kw hello hello\',那么下次发送hello时,将会自动回复hello。\
(注意，键和值内不应包含空格)\n\n\
4.根据上面2生成的内容,发送对应键,即可回复'))