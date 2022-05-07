
from nonebot import require
import nonebot
from nonebot.adapters.onebot.v11.message import Message
import os
from random import randint
from apscheduler.triggers.combining import AndTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger

scheduler = require('nonebot_plugin_apscheduler').scheduler

# 读取本地的随机图片目录
def get_one_image_from_local(dir):  
    files = os.listdir(dir)
    n = len(files)
    index = randint(0,n)
    image_dir = os.path.join(dir,files[index])  
    image_dir = image_dir.replace("\\","/")
    return image_dir

@scheduler.scheduled_job('cron', hour=7,minute=00)
async def demo():
    bot = nonebot.get_bot()
    dir = "C:/好图" 
    group_id = [858125778,907423953]
    img_dir = get_one_image_from_local(dir)
    for i in range(len(group_id)):
        await bot.send_group_msg(group_id=group_id[i],message=Message(f'早上好各位，今天又是元气满满的一天呢！[CQ:image,file=file:///{img_dir}]'))

