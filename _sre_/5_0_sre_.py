#coding=utf-8

什么是正则表达式？
正则表达式是一种文本模式,用于[搜索]文本时要[匹配]的[一个]或[多个]字符串。

正则表达式的语法
. 匹配任意字符
\d 匹配数字
\w 匹配字符[a-zA-z0-9]
\s 匹配空格
\ 转义字符
* 匹配零次或多次	
+ 匹配一次或多次	
? 匹配零次或一次
*? 非贪婪匹配
贪婪匹配的意思是，在同一个匹配项中，尽量匹配更多所搜索的字符，
非贪婪则相反。

正则上手：http://www.regexr.com/

测试文本：
<span>开业后的第一个周末，SKP南馆就被“挤爆”了。</span><span>12月14日，一个寒冷的北京清晨，你很难想象一向给人高冷印象的奢侈品商场会涌进这么多的人：大家忙着拍商场入口处非常逼真的仿生绵羊、忙着参观国内首家Gucci美妆体验店、忙着在Gentle Monster全球首家咖啡店里品尝被做成人体器官造型的甜品、忙着在馆内的艺术雕塑旁边拗造型拍大片，购物这件事反而被放在了一边。</span>
<img src="https://img.163.com/icon.jpg" />









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




