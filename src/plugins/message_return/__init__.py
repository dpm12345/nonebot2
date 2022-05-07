
from multiprocessing import Event
import mysql.connector
from nonebot import on_message
from nonebot.adapters.onebot.v11.message import Message
from nonebot.adapters.onebot.v11 import Bot,Event
import re


# 权限设置
permisson = ("qq号","qq号")


# 对传入数据进行操作,分为一个列表
def spearate(str):
  res = re.split(" ",str)
  for i in range(res.count('')):
    res.remove('')
  return res

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
def insert(mydb,mycursor,keyword,response):
  sql = "INSERT INTO return_response (keyword,response) VALUES (%s, %s)"
  val = (keyword,response)
  if search(mydb,mycursor=mycursor,keyword=keyword) == 1 :
    return 0
  else:
    mycursor.execute(sql, val)
    mydb.commit()    # 数据表内容有更新，必须使用到该语句
    return 1

# 删除数据操作
def delete(mydb,mycursor,keyword):
  if search(mydb=mydb,mycursor=mycursor,keyword=keyword) == 1:
    sql = "DELETE FROM return_response WHERE keyword='%s'"%keyword
 
    mycursor.execute(sql)
 
    mydb.commit()
    return 1
  else:
    return 0

# 更新
def upgrade(mydb,mycursor,keyword,new_response):
  if search(mydb=mydb,mycursor=mycursor,keyword=keyword) == 1:
    sql = f"UPDATE return_response SET response='{new_response}' where keyword='{keyword}'"
  
    mycursor.execute(sql)
    mydb.commit()
    return 1
  else:
    return 0

res = on_message(priority=10,block=False)


@res.handle()
async def res_send(bot: Bot, event: Event):
    ans = ""
    mydb = mysql.connector.connect(
    host="localhost",       # 数据库主机地址
    user="root",     # 数据库用户名
    passwd="root12",   # 数据库密码
    database="robot"
  )
 
    mycursor = mydb.cursor()
    mess = spearate(str(event.get_message()))
    user_id = event.get_user_id()
    
    # 插入数据
    if len(mess)==0:
      await res.finish(Message("到"))
    if mess[0] == "kw":
      if len(mess) != 3:
        await res.send(Message(f"[CQ:at,qq={user_id}]请输入kw + 键 + 对应值(键、值内不应包含空格)"))
      keyword = mess[1]
      response = mess[2]
      if insert(mydb=mydb,mycursor=mycursor,keyword=keyword,response=response) == 1:
          await res.send(Message(f"[CQ:at,qq={user_id}]我记住了[CQ:face,id=287]"))
      else:
        await res.send(Message(f"[CQ:at,qq={user_id}]数据已存在，请使用upgrade进行数据更新"))
    elif mess[0] == "upgrade":
      if len(mess) != 3:
        await res.send(Message(f"[CQ:at,qq={user_id}]请输入upgrade + 键 + 新对应值(键、值内不应包含空格)"))
      keyword = mess[1]
      new_response = mess[2]
      if user_id in permisson:
        if upgrade(mydb=mydb,mycursor=mycursor,keyword=keyword,new_response=new_response) == 1:
          await res.send(Message(f"[CQ:at,qq={user_id}]更新完成[CQ:face,id=287]"))
        else:
          await res.send(Message(f"[CQ:at,qq={user_id}]数据不存在"))
      else:
        await res.send(Message(f"[CQ:at,qq={user_id}]无权限更新"))
    # 删除操作
    elif mess[0] == "del":
      if len(mess) == 2:
        keyword = mess[1]
        if user_id in permisson:
          if delete(mydb=mydb,mycursor=mycursor,keyword=keyword) == 1:
            await res.send(Message(f"[CQ:at,qq={user_id}]删除成功[CQ:face,id=287]"))
          else:
            await res.send(Message(f"[CQ:at,qq={user_id}]该值不存在"))
        else:
          await res.send(Message(f"[CQ:at,qq={user_id}]无权限删除"))
      else:
        await res.send(Message(f"[CQ:at,qq={user_id}]请输入\'del+你要删除的关键字\'"))
    elif len(mess) == 1:
      keyword = mess[0]
      if re.match("^这就是", keyword):
        await res.send(Message(keyword))
      elif search(mydb=mydb,mycursor=mycursor,keyword=keyword) == 1:
        sql = f"SELECT response FROM return_response where keyword='{keyword}'"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        ans = myresult[0]
        await res.send(Message(ans))
      



    
    
    






