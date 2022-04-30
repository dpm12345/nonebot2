
import requests
import re

# api = "https://iw233.cn/api.php?sort=random&type=json"
# response = requests.get(api)
# url = response.text[8:-2]
# print(url)

with open("C:/Users/10069/Desktop/1.jpg",mode="wb") as file:
    file.write(requests.get("https://tvax1.sinaimg.cn//large//ec43126fgy1gxqinevnfkj23gv0sx4qr.jpg").content)

# api = "https://iw233.cn/api.php?sort=random&type=json"
# raw_url = requests.get(api).text[8:-2]
# pic_url = re.sub("\/", "", raw_url)

# print(pic_url)