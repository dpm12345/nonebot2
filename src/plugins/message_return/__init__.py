# from nonebot import on_message, logger
# from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent
# from . import config
# import re

# repeater_group = config.repeater_group
# shortest = config.shortest_length

# m = on_message(priority=10, block=False)

# last_message = {}
# message_times = {}


# # 消息预处理
# def messagePreprocess(message: str):
#     raw_message = message
#     contained_images = {}
#     images = re.findall(r'\[CQ:image.*?]', message)
#     for i in images:
#         contained_images.update({i: [re.findall(r'\[.*url=(.*?),.*]', i)[0], re.findall(r'\[.*file=(.*?),.*]', i)[0]]})
#     for i in contained_images:
#         message = message.replace(i, f'[{contained_images[i][1]}]')
#     return message, raw_message


# @m.handle()
# async def repeater(bot: Bot, event: GroupMessageEvent):
#     gid = str(event.group_id)
#     if gid in repeater_group:
#         global last_message, message_times
#         message, raw_message = messagePreprocess(str(event.message))
#         logger.debug(f'这一次消息: {message}')
#         logger.debug(f'上一次消息: {last_message.get(gid)}')
#         if last_message.get(gid) != message:
#             message_times[gid] = 1
#         else:
#             message_times[gid] += 1
#         logger.debug(f'已重复次数: {message_times.get(gid)}')
#         if message_times.get(gid) >= config.shortest_times:
#             logger.debug(f'原始的消息: {str(event.message)}')
#             logger.debug(f"欲发送信息: {raw_message}")
#             await bot.send_group_msg(group_id=event.group_id, message=raw_message, auto_escape=False)
#         last_message[gid] = message

from multiprocessing import Event
import mysql.connector
from nonebot import on_message
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import Bot,Event
import re

# 检查数据类型
def return_data_type(message_type):
  if message_type == 'text':
    return 'text'
  elif message_type == 'face':
    return 'id'

# 对传入数据进行操作,转为CQ码
def spearate(str):
  res = re.split(" ",str)
  for i in range(res.count('')):
    res.remove('')
  return Message(res)

# 查询数据操作
def search(mydb,mycursor,keyword):
  sql = "SELECT response FROM return_response where keyword='%s'"%(keyword)
  mycursor.execute(sql)
  myresult = mycursor.fetchall()     # fetchall() 获取所有记录
  if len(myresult)>0:
    return 1
  else:
    return 0

# 插入数据操作
def insert(mydb,mycursor,type1,keyword,type2,response):
  sql = "INSERT INTO return_response (type1,keyword,type2,response) VALUES (%s, %s, %s, %s)"
  val = (type1,keyword,type2,response)
  if search(mydb,mycursor=mycursor,keyword=keyword) == 1 :
    return 0
  else:
    mycursor.execute(sql, val)
    mydb.commit()    # 数据表内容有更新，必须使用到该语句
    return 1

# 删除数据操作
def delete(mydb,mycursor,keyword):
  sql = "DELETE FROM return_response WHERE keyword='%s'"%keyword
 
  mycursor.execute(sql)
 
  mydb.commit()
  return 1

res = on_message(priority=10,block=False)

@res.handle()
async def res_send(bot: Bot, event: Event):
    ans = ""
    mydb = mysql.connector.connect(
    host="localhost",       # 数据库主机地址
    user="root",     # 数据库用户名
    passwd="root",   # 数据库密码
    database="robot"
  )
 
    mycursor = mydb.cursor()
    mess = spearate(str(event.get_message()))
    
    # 插入数据
    if mess[0].type == 'text' and mess[0].data['text'] == "kw":
      if len(mess) != 3:
        await res.send("请输入kw + 键 + 对应值(键、值内不应包含空格)")
      type1 = mess[1].type
      keyword = mess[1].data[return_data_type(type1)]
      type2 = mess[2].type
      response = mess[2].data[return_data_type(type2)]
      if search(mydb=mydb,mycursor=mycursor,keyword=keyword) == 0:
        if insert(mydb=mydb,mycursor=mycursor,type1=type1,keyword=keyword,type2=type2,response=response) == 1:
          await res.send("我记住了")
      else:
        await res.send("无权修改")

    elif len(mess) == 1:
      keyword = mess[0].data[return_data_type(mess[0].type)]
      if search(mydb=mydb,mycursor=mycursor,keyword=keyword) == 1:
        sql = f"SELECT type2,response FROM return_response where keyword='{keyword}'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        ans_type = myresult[0][0]
        ans_data_type = return_data_type(ans_type)
        ans_data_data = myresult[0][1]
        if ans_type == "text":
          ans = ans_data_data
        else:
          ans = f"[CQ:{ans_type},{ans_data_type}={ans_data_data}]"
        
        await res.send(Message(ans))
      elif re.match("^这就是", keyword):
        await res.send(Message(keyword))
      



    
    
    






