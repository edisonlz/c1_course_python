a = [1,2,3,4,5,6]

#数组的基本迭代
for i in a:
    print(i)

#迭代器
for i in range(10):
    print(i)

range(start,end,step)
start 开始
end 结束
step 步长

for i in range(0,len(a),2):
    print(i , end=',')


