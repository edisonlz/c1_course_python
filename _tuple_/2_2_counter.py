怎样找出一个序列中出现次数最多的元素呢？


问：假设你有一个单词列表并且想找出哪个单词出现频率最高?

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

print(words)
from collections import Counter
word_counts = Counter(words)
# 出现频率最高的3个单词

top_three = word_counts.most_common(3)
print(top_three)

