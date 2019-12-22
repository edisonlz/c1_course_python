循环

如何获取一个数组中的偶数？

a = [1,2,3,4,5,6]

循环控制语句语法

语法1
for element in elements:
    print(element)

语法2 
通过下标索引进行循环
for i in range(len(elements)):
    element = elements[i]
    print(i,element)

语法3
b = [ element for element in elements if 条件判断 ]
b = [ element for element in elements if element % 2 == 0 ]


关键字
break 终止循环
continue 结束本次循环，开始下次循序


1）打印如果 element == 3 终止循环 break
2）只打印奇数 continue


语法4 while

while 判断条件为 True|False:
    执行代码











