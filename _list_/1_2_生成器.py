生成器
1. 什么是生成器：
1）生成器是一个返回迭代器的函数，
2) 只能用于迭代操作，更简单点理解生成器就是一个迭代器。
3) 优点只有迭代时才进行计算，节省内存空间


把列表里的值 + 100 ，如果这个列表长度为100万那？

L = [x + 100 for x in range(10)]

g = (x + 100 for x in range(10))


2. yield
1）遇到yield关键字就会中断并返回yield定义的变量
2) 下次再调用，就会从上次中断的地方继续执行，直到下一个yield关键字

def test():
    for i in range(3):
        yield i

f = test()

for i in range(3):
    print(f.__next__())


3. 接受参数send

def test_send():
     print("等待接受任务")
     while True:
          data = yield
          print("成功接受任务：",data)


f = test_send()
f.__next__()
f.send(10)



