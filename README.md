# nonebot2-plugin

基于nonebot2写的机器人插件



# 本人介绍

本人是位python小白，觉得qq机器人很酷，便尝试着写一下

# 功能实现

## 随机数生成

通过使用random命令，来进行随机数的生成(目前只生成int类型)，用户自定义随机数的范围及生成随机数的个数

如命令`/random 1 10 2`即生成2个1~10的整数

目前只支持群里的随机数生成，需要在命令前@机器人

## 对指定消息的自动回复

这项功能的实现想法主要来自于ctfshow中的机器人大牛，每次会根据消息来回复，同时这也是我开始编写机器人的想法的来源

在实现这项功能时，为了能够存储需要自动恢复的消息，我在这里采用了与数据库连接的想法，当出现某个消息时，利用MySQL的select查询语句，判断并返回相应的值，用于回复

在这里，为了能够丰富指定的消息，这里支持自定义回复消息，通过聊天窗口需要发送的语句为`kw 指定消息 回复消息`

数据库的设置
```
数据库名：robot
编码方式:utfmb4
表名: return_message
字段名及属性:   id          mediumint 11
               keyword     longtext         utf8mb4
               response    longtext         utf6mb4
```
请在自己的服务器上建立以上数据库内容，若自定义，请在以下部分进行修改
```
mydb = mysql.connector.connect(
    host="yoursever",       # 数据库主机地址
    user="yourname",     # 数据库用户名
    passwd="yourpassword",   # 数据库密码
    database="name"          # 数据库名
  )
# 查询数据操作
sql = "SELECT 回复消息对应字段 FROM 你的表名 where 指定消息对应字段='%s'"%(keyword)

# 插入数据操作
sql = "INSERT INTO 你的表名 (指定消息对应字段,回复消息对应字段) VALUES (%s, %s)"

# 删除数据操作
sql = "DELETE FROM 你的表名 WHERE 指定消息对应字段='%s'"%keyword

# 更新
sql = f"UPDATE 你的表名 SET 回复消息对应字段='{new_response}' where 指定消息对应字段='{keyword}'"

```
对于可进行修改的用户，请在代码最前面修改permission中的内容，填入允许的qq号
如下，则允许用户qq=1223，2212进行更新和删除工作
```
permisson = ("1223","2212") 
```


## 今日人品运数生成

该功能的实现是完全使用[Well404大佬的代码(点我)](https://github.com/Well2333/NoneBot2_NoobGuide/blob/master/%E7%AC%AC%E4%BA%8C%E7%AB%A0%20%E5%9F%BA%E7%A1%80%E6%8F%92%E4%BB%B6%E7%BC%96%E5%86%992%E2%80%94%E2%80%94%E5%90%AC%E5%BE%97%E8%A7%81%EF%BC%8C%E8%AF%B4%E5%BE%97%E5%87%BA.md),建议直接去那里看


## 随机发图功能

这里分为美图和涩图两大类(ACG)，一部分来源于自己的存货，一部分来源于api。
在使用时请改变图片路径
```
dir = your_path
```
这里感谢[MirlKoi](https://iw233.cn/)api的提供

使用该命令时需@机器人，并以'/'作为命令起始
命令如下
1. 美图:"random_pic1"/"随机美图"/"来张美图"/"美图"
2. 涩图:"random_pic2"/"随机涩图"/"来张涩图"/"涩图"/"随机色图"/"来张色图"/"色图"



机器人将会自动发送图片


# 期望

不断学习，完善和加入更多功能
