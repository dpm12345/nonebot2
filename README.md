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

(目前仅支持纯文字和表情的内容存储，其中`指定消息`和`回复消息`都只能是同一种类型，即不能同时包含文字和表情,日后会尝试解决这一限制)

(同时，目前仅支持设置内容，不支持修改内容和删除内容，日后会找时间完善)

## 今日人品运数生成

该功能的实现是完全使用[Well404大佬的代码(点我)](https://github.com/Well2333/NoneBot2_NoobGuide/blob/master/%E7%AC%AC%E4%BA%8C%E7%AB%A0%20%E5%9F%BA%E7%A1%80%E6%8F%92%E4%BB%B6%E7%BC%96%E5%86%992%E2%80%94%E2%80%94%E5%90%AC%E5%BE%97%E8%A7%81%EF%BC%8C%E8%AF%B4%E5%BE%97%E5%87%BA.md),建议直接去那里看


## 随机发图功能

这里分为美图和涩图两大类(ACG)，一部分来源于自己的存货，一部分来源于api。
这里感谢[MirlKoi](https://iw233.cn/)api的提供

使用该命令时需@机器人，并以'/'作为命令起始
命令如下
1. 美图:"random_pic1"/"随机美图"/"来张美图"/"美图"
2. 涩图:"random_pic2"/"随机涩图"/"来张涩图"/"涩图"

机器人将会自动发送图片


# 期望

不断学习，完善和加入更多功能
