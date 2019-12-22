元组(tuple)为不可更改数组

元组的定义
a = tuple()
a = ()

元组(tuple)和列表(list)区别

最主要的两个区别
1. 元组不能修改
2. 元组占用内存更小


a = tuple(range(1000))
b = list(range(1000))
print("a.size:%s,b.size:%s" % (a.__sizeof__() ,b.__sizeof__()))

