
字典 dict

知识点
1.字典是基于[数组]的高级数据结构
2.key : value
3.数组通过下标进行快速的索引到值，a = [1,2,3] , a[1]
  字典可以通过key快速的索引到值  dic = {"key":"value"}
  dic["key"] , 这里的 key 的类型可以是str，float，int, hashable object
  
字典的定义
dic = dict()
dic = dict(one=1, two=2, three=3)
dic = dict({'three': 3, 'one': 1, 'two': 2})
dic = {}
dic = {'three': 3, 'one': 1, 'two': 2}

字典方法
赋值的2中方法
dic.update({'six':6})
dic['ten'] = 10

读取值的两种方法
dic['three']
dic['one']
dic['four']
dic.get('four')

删除值的两种方法
del dic[key]
dic.pop('four')

len(dic)
key in dic
key not in dic
dic.clear()

字典的遍历
for key,value in dic.items():
    print("%s = %s" % (key,value))



