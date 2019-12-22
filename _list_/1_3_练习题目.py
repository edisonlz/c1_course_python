#coding=utf-8

---------------------------------------------
1. 打印99乘法表

for i in range(1,10):
    print('',end='\n')
    for j in range(1,i+1):
        print("%d * %d = %d" %(i , j , i*j) ,end=",")


---------------------------------------------
2. Fibonacci, 斐波那契数列, 求第N步等于多少
公式 F[n]=F[n-1]+F[n-2] 0 1
n1 = 0
n2 = 1
step = 10
n = 0
for i in range(step):
    #print("%d+%d=%d" % (n1,n2,n1+n2))
    print(n,end=",")
    n = n1 + n2
    n1 = n2 
    n2 = n
print(n)


---------------------------------------------
3. 二分查找，折半查找
 1）数组是有序的
 2）利用下标从(中间)开始查找 ，记录开始，结束下标位置
    如果下标处数值大于查找值，结束下标= mid-1 
    如果下标处数值小于查找值，开始下标= mid+1 
    返回条件：1.找到对应数值，2.开始下标>结束下标返回
             4
             4    6      
    0             6
    start         end
a = [1,2,3,4,5,6,7]

start = 0
end = len(a) - 1
find_number = 5

while start<=end:
    #计算数组中间下标位置
    
    mid = int((start+end)/2)
    print("start:%s,end:%s,mid:%s" % (start,end,mid))
    data = a[mid]
    if data > find_number:
        end = mid - 1
    elif data < find_number:
        start = mid + 1
    else:
        print("index is :%s" % mid)
        break






    






        





























---------------------------------------------
4. 平衡点问题,
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
    
    print("sum_start:%s,sum_end:%s,start:%s,end:%s" % (sum_start,sum_end,start,end))
    if sum_start == sum_end:
        if start==end:
            print("平衡点为:%s" %a[start])
            break


    
    
