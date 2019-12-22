
什么是序列化，为什么需要序列化？
  统一异构系统数据通信规则

NSDictionary     HashMap       Object

  Object-C       Java      JavaScript
    IOS         Android      Chrome，IE
   _____       ———————     ————————————
   |   |       | — — |     |          |
   |   |       |     |     |          |
   | O |       |     |     |          |
   _____       ———————     |          |
                           ————————————
                   |
                   |
              |  data  |
                   |
                   |
                   |
                 Server
                [Python]
                  dict


response = {
    "username":"ed",
    "msg":"hello world",
    "sex": 1,
    "balance":102.2
}



import json
json.dumps(response)
reponse_string = json.dumps(response)
type(reponse_string)
response = json.loads(reponse_string)
type(response)

