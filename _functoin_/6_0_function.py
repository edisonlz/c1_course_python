
1.函数的定义
def 定义函数关键字

show 函数名称
(me) 参数
return 返回值


def show(me):
    print("%s is here!" % me)
    return "Done"
    
show("ed")


2.函数接受任意数量的位置参数，可以使用一个 * 参数

def avg(first, *rest):
    print(first)
    print(rest)
    print(type(rest))
    return (first + sum(rest)) / (1 + len(rest))
    
avg(1, 2, 3, 4) 

3.接受任意数量的关键字参数，使用一个以 ** 开头的参数

def request_to_query(**params):
    """
    生成HTTP请求参数
    """
    print(params)
    print(type(params))

    qs = []
    for key,value in params.items():
        qs.append("%s=%s"%(key,value))
    print(qs)
    result = "&".join(qs)
    return result

request_to_query(web="chrome",id=2,username="ed")

    

4. help 打印方法帮助信息
help(request_to_query)

5. 返回多个值的函数,解包
def myfun():
    return 1, 2, 3

a,b,c = myfun()  
print("a=%d , b=%d , c=%d" % (a,b,c))

6.定义有默认参数的函数
def sums(a,b=10):
    print("%d+%d=%d" % (a,b,a+b))
    return a+b

s = sums(1, 2)
print("s=%d"% s)
s = sums(1)
print("s=%d"% s)

        

7.定义匿名函数,lambda 关键字
add = lambda x, y: x + y 
add(2,3)
add('hello', 'world')



