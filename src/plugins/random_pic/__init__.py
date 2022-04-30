
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11.message import Message,MessageSegment
from nonebot.adapters.onebot.v11 import Event, Bot
import os
from random import randint

random_pic1 = on_command("random_pic1",aliases={"随机美图","来张美图","美图"},block=False,rule=to_me())
random_pic2 = on_command("random_pic2",aliases={"随机涩图","来张涩图","涩图",},block=False,rule=to_me())

# 读取本地的随机图片目录
def get_one_image_from_local(dir):  
    files = os.listdir(dir)
    n = len(files)
    index = randint(0,n)
    image_dir = os.path.join(dir,files[index])  
    image_dir = image_dir.replace("\\","/")
    return image_dir



@random_pic1.handle()
async def _(bot: Bot,event: Event):
    dir = "C:\好图" 
    img_dir = get_one_image_from_local(dir)
    api = "https://iw233.cn/api.php?sort=iw233"
    choose = randint(0,1)
    if choose == 0:
        await random_pic1.send(Message(f'[CQ:at,qq={event.get_user_id()}][CQ:image,file={api},cache=0,proxy=0]'))
    else:
        await random_pic1.send(Message(f'[CQ:at,qq={event.get_user_id()}][CQ:image,file=file:///{img_dir}]'))
@random_pic2.handle()
async def _(bot: Bot,event: Event):
    dir = "C:\涩图" 
    img_dir = get_one_image_from_local(dir)
    api = "http://iw233.fgimax2.fgnwctvip.com/API/Ghs.php"
    choose = randint(0,1)
    if choose == 0:
        await random_pic2.send(Message(f'[CQ:at,qq={event.get_user_id()}][CQ:image,file={api},cache=0]'))
    else:
        await random_pic2.send(Message(f'[CQ:at,qq={event.get_user_id()}][CQ:image,file=file:///{img_dir}]'))