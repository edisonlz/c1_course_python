
1. 问:怎样在两个字典中寻寻找相同点?

a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'y' : 2,
    'z' : 3,
}

print(a.keys() & b.keys())




2.问：假设你有一个单词列表并且想找出哪个单词出现频率最高?

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
print(words)


dic = {}

for word in words:
    if word not in dic:
        dic[word] = 0
    
    dic[word] += 1
    
print(dic)

sorted(dic.items(), key=lambda item:item[1],reverse=True)





















# for word in words:
#     if word not in dic:
#         dic[word] = 0
#     dic[word] += 1
    
# print(dic)

# #字典排序
# sorted(dic.items(), key=lambda item:item[1],reverse=True)





