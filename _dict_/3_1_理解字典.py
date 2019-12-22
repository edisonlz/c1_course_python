
理解字典

知识点 
1.字典是基于【数组】的高级数据结构 - 哈希表
2.key : value
3.数组通过下标进行快速的索引到值，a = [1,2,3] , a[1]
  字典可以通过key快速的索引到值  dic = {"key":"value"}
  dic["key"] , 这里的 key 的类型可以是str，float，int, 
  hashable object
  object.__hash__()
  

1.字典是一个长度[固定]的[数组]，数组的内容是一个链表
list_length = 10
dic = [''] * list_length

dic['obj'] = "value"
2） 这里key是字符串类型，我们如何将字符串转化int类型的数组下标
通过我的 hash() 方法
index = hash('obj')

3) index的值过于大如何如何解决
dic[108529808729698265] =  "value"
index = index % list_length 求余数
index = 5
dic[5] = "value"

*重要*：key转换为下标的索引的【公式】：
key = "obj"
value = "value"
index = hash(key)
index = index % list_length
dic[index] = value
print(dic)

4）如果其他key值通过求余算法也等于5如何处理,
这种情况称之为key值冲突
2种处理方法:  
        1.在哈希 hash(key) + 1
        2.链表 *

 ----------------------------------------
 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
 ----------------------------------------
   |                   |
   链表               链表
   key1              'obj' : hash('obj') = 108529808729698265
   key100             5 :  hash(5) = 5
                   

 


