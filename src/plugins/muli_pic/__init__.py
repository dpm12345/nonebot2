from multiprocessing import Event
from time import sleep
from nonebot.rule import to_me
from nonebot import on_startswith
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import Bot,Event
from nonebot.params import  ArgPlainText
import os
from random import randint
import requests

# cmd = ("涩图","来几张涩图","色图","来几张色图")
ne = on_startswith(("涩图","来几张涩图","色图","来几张色图"),rule=to_me())

def get_one_image_from_local(dir):  
    files = os.listdir(dir)
    n = len(files)
    index = randint(0,n)
    image_dir = os.path.join(dir,files[index])  
    image_dir = image_dir.replace("\\","/")
    return image_dir

def return_pic():
    
    choose = randint(0,1)
    if choose == 0:
        api = "http://iw233.fgimax2.fgnwctvip.com/API/Ghs.php?type=json"
        img_url = requests.get(api).text[8:-2].replace("\\","")
        return f'[CQ:image,file={img_url},cache=0]'
    else:
        dir = "C:/涩图" 
        img_dir = get_one_image_from_local(dir)
        return f'[CQ:image,file=file:///{img_dir}]'

@ne.handle()
async def _(bot:Bot,event:Event):
    pass

@ne.got("num",prompt="几张图呢")
async def send_pic(bot:Bot,event:Event,num:str = ArgPlainText("num")):
    num1 = float(num)
    num2 = int(num1)
    total = f"[CQ:at,qq={event.get_user_id()}]"
    

    if not num1 == num2:
        await ne.finish("图片怎么会有小数呢")
    
    if num1 < 0:
        await ne.finish(Message(f"[CQ:at,qq={event.get_user_id()}]快点给我发{abs(num2)}张涩图[CQ:face,id=277]"))
    elif num2 <=5 and num2 > 0:
        for i in range(num2):
            total += return_pic()
            sleep(0.2)
        
        await ne.finish(Message(total +"满意吗？"))
    elif num2 > 5:
        await ne.finish("一次不能超过5张图")
    else:
        await ne.finish(Message("既然不想要涩图为什么要@我呢[CQ:face,id=9]"))