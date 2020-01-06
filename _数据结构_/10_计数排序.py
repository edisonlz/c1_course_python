
问题：在一个无序数组中找到第K个最大的元素，线性时间？

假设：数组最大值在有限范围，及最大值不超过数组长度。

计数排序 Counting Sort 
线性排序时间，时间复杂度 O(N + K)

a = [4 , 3 , 2 , 1,  4]

步骤1. 初始化数组 ，长度len(a),默认值0
步骤2. 数组元素作为索引，对应的值+1，目的是记录重复次数
步骤3. 从第二个元素开始累加前一个元素值
步骤4. 根据元组元素分配,分配后counter对应的值减1，最终位置


counter = [0, 0, 1, 2, 4]

target = [1, 2, 3, 4, 4]




a = [4 , 3 , 2 , 1,  4]

counter = []
target = []

for i in range(len(a)):
    counter.append(0)
    target.append(0)

for data in a:
    counter[data]+=1

for j in range(1,len(counter)):
    counter[j] = counter[j] + counter[j-1]


for data in a:
    index = counter[data]
    target[index-1] = data
    counter[data] -= 1

print(target)




























































# 1)
#         ------------------
# counter 0 , 0 , 0 , 0 , 0
#         ------------------
# 2)
#         ------------------
# counter 0 , 1 , 1 , 1 , 2
#         ------------------
# 3)
#         ------------------
# counter 0 , 1 , 2 , 3 , 5
#         ------------------
# 4)
# a = [4 , 3 , 2 , 1, 4]

#         ------------------
# counter 0 , 0 , 1 , 2 , 3
#         ------------------

#         ------------------
# target  1 , 2 , 3 , 4 , 4
#         ------------------


# 代码实现


# a = [4 , 3 , 2 , 1, 4]

# counter = []
# target = []

# for i in range(len(a)):
#     counter.append(0)
#     target.append(0)

# for i in a:
#     counter[i]+= 1

# for j in range(1,len(a)):
#     counter[j] = counter[j] + counter[j-1]


# for data in reversed(a):
#     index = counter[data]
#     target[index-1] = data
#     counter[data] -= 1

# print(target)


