文件操作

1.读取文件
语法： open(file,mode)
file：文件路径
mode: r is read  读取文本
      r+  可读写，可以写到文件任何位置 
      w is write 写入文本，覆盖原有内容
      w+ 可读写，覆盖原有内容
      a is append 追加的末尾
      a+ 可读写，只能写在文件末尾 

f = open('./somefile.txt', 'w')
data = f.read()
print(data)
f.close()


with open('./somefile.txt', 'r') as f: 
    data = f.read()
    print(data)
    #f.close() 自动执行


2.读取压缩文件
# gzip compression
import gzip
with gzip.open('/Users/winlesson/c1_course_python/_file_/somefile.txt.tar.gz', 'rt') as f:
    text = f.read()
    print(text)


3.写入文件
with open('./somefile.txt', 'w+') as fd: 
    fd.write('hello word\n')
    fd.write('hello china\n')


3.获取当前文件路径
import os, sys

file_path = os.path.abspath(__file__)
dir_path = os.path.dirname(__file__)

print(file_path)
print(dir_path)
out_path = os.path.join(dir_path,'somefile.txt')
print(out_path)

f = None
try:
    f = open(out_path, 'w+')
    f.write('hello word')
except Exception,e:
    print(e)
finally:
    if f:
        f.close()




