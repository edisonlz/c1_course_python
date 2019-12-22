正则表达式应用

题： 获取百度贴吧的图片地址？

import re
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://tieba.baidu.com/p/1457328558#!/l/p1"


req = urllib.request.urlopen(url)
body = req.read()
print(body)

pattern_image = b'src="(.*?\.jpg)"'
matchs = re.findall(pattern_image, body)

for match in matchs:
    print(match)




https://imgsa.baidu.com/forum/abpic/item/a13cf8dcd100baa1698a91ee4710b912c9fc2ec6.jpg





