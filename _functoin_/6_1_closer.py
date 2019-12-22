
问：如何调用一个函数，使其每次输出自动+1？

知识点
1) 闭包：闭包就是能够读取其他函数内部变量的函数
2) nonlocal 关键字用来在函数内使用外层变量

def auto_add():
    n = 0
    def add():
        nonlocal n
        n+=1
        return n
    return add

auto_plus = auto_add()


























# def auto_sum():
#     d = 0
#     def add():
#         nonlocal d
#         d+=1
#         return d
#     return add


# add = auto_sum()

