#coding=utf-8

1. 打印99乘法表
for i in range(1,10):
    print('')
    for j in range(1,i+1):
        print("%d * %d = %d, " % (i, j, i*j),end='')
print('')



2. Fibonacci, 斐波那契数列, 求第N步等于多少
公式 F[n]=F[n-1]+F[n-2]

n1 , n2 = 0 , 1
for i in range(10):
    print(n2, end=',')
    n = n1 + n2
    n1 = n2
    n2 = n
 
3. 二分查找，折半查找
 1）数组是有序的
 2）利用下标从中间开始查找 ，记录开始，结束下标位置
    如果下标处数值大于查找值，结束下标= mid-1 
    如果下标处数值小于查找值，开始下标= mid+1 
    返回条件：1.找到对应数值，2.开始下标>结束下标返回
    
a = [2,4,6,8,10]
start = 0
end = len(a) - 1 
find_num = 4
while start<=end:
    mid = int((start + end)/2)
    data = a[mid]
    print("start:%s,end:%s,mid:%s,find_num:%s,data:%s" % (start,end, mid,find_num,data))
    
    if data>find_num:
        end = mid - 1
    elif data<find_num:
        start = mid + 1
    else:
        print("下标为：%d" % mid)
        break

    
       
4. 平衡点问题
一个数组中的元素，前面部分的和等于后面的部分
例如 numbers = [1, 3, 5, 2, 2]，其中5位平衡点
前后元素之和相等,值为4

     0  1  2  3  4
a = [1, 3, 5, 2, 2]
     i           j
     1           2
        4        2
        4     4
           |

start = 0
end = len(a) - 1
sum_start = 0
sum_end = 0

while start<=end:
    if sum_start<sum_end:
        sum_start+=a[start]
        start+=1
    else:
        sum_end+=a[end]
        end-=1

    print("%s:%s" % (sum_start,sum_end))
    if sum_start == sum_end:
        if start==end:
            print("平衡点为:%s" %a[start])
            break


    
    
