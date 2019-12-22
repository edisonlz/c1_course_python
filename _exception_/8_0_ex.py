异常

捕获异常语法:

try:
    执行代码
except expression as e:
    异常处理
else:
    print("正常运行")
finally:
    print("异常或正常都会执行")



1. 基本语法示例
try:
    #f = open("missing")
    f = 1 + 2
except Exception as e:
    print(e)
else:
    print("正常运行")
finally:
    print("异常或正常都会执行")


2.捕获多种异常
try:
    f = open('missing') 
except OSError as e:
    print(e) 
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)




3.抛出异常
try:
    raise Exception("错误了")
except Exception as e:
    print(e) 




