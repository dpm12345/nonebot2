
from random import randint
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import Event, Bot
import re
ran_num = on_command("random",aliases={"随机数"},priority=2,rule=to_me(),block=False)

@ran_num.handle()
async def generate(bot: Bot, event: Event):
    qq_id = event.get_user_id()
    data = str(event.get_message())
    data = re.split(" ",data)
    for i in range(data.count('')):
        data.remove('')
    res = []
    for i in range(int(data[-1])):
        res.append(randint(int(data[1]),int(data[2])))
    await ran_num.finish(Message(f"[CQ:at,qq={qq_id}]生成的随机数为\n{res}"))


