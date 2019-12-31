线性数据结构: 队列


队列是一种操作受限的线性表仅允许在表的一端进行插入，
而在表的另一端进行删除，队尾入队，对头出队。
队列有两种存储方式，即数组和链表。

FIFO（先进先出）

         ------------------------
[head]   |1 | 2 | 3 | 4 | 5 | 6 |   [tail]
dequeue  ------------------------   enqueue
  出队                                入队

class Queue(object):

  def __init__(self):
    self.queue = []

  def enqueue(self,data):
    self.queue.append(data)
    
  def dequeue(self):
    if self.queue:
      return self.queue.pop(0)

queue = Queue()


线性数据结构: 栈
栈是一种操作受限的线性表只允许从一端插入和删除数据。
栈有两种存储方式，即数组和链表。
LIFO（后进先出）

入栈        出栈
 ↑  |  5  |  ↓
    |  4  |
    |  3  |
    |  2  |
    |  1  |
    ———————

class Stack(object):
  
  def __init__(self):
    self.stack = []

  def push(self,data):
    self.stack.append(data)

  def pop(self):
    if self.stack:
      return  self.stack.pop()


stack = Stack()

    

    
































# class Queue(object):

#     def __init__(self):
#         self.queue = []

#     def enqueue(self,data):
#         #入队
#         self.queue.append(data)

#     def dequeue(self):
#         #出队并返回出队的值
#         if self.queue:
#             return self.queue.pop(0)

# queue = Queue()



# class Stack(object):
    
#     def __init__(self):
#         self.stack = []

#     def push(self,data):
#         self.stack.append(data)

#     def pop(self):
#         if self.stack:
#             return self.stack.pop()

# stack = Stack()

