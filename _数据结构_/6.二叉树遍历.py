
tree = ["A","B","C","D","E","F","G"]

        A
      /   \
     B     C
    /\     /\
   D   E  F  G


class Node(object):

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


    def add_left_child(self, node):
        self.left = node

    def add_right_child(self , node):
        self.right = node


class Tree(object):

    def __init__(self, node):
        self.root = node


root = Node("A")
tree = Tree(root)
node_b = Node("B")
node_c = Node("C")

root.add_left_child(node_b)
root.add_right_child(node_c)


node_d = Node("D")
node_e = Node("E")
node_b.add_left_child(node_d)
node_b.add_right_child(node_e)

node_f = Node("F")
node_g = Node("G")
node_c.add_left_child(node_f)
node_c.add_right_child(node_g)


广度优先搜索, 使用队列实现

class Queue(object):

    def __init__(self):
        self.queue = []

    def enqueue(self,data):
        #入队
        self.queue.append(data)

    def dequeue(self):
        #出队并返回出队的值
        if self.queue:
            return self.queue.pop(0)


queue = Queue()

queue.enqueue(root)
child = queue.dequeue()
while child:
    print(child.data,end=",")

    if child.left:
         queue.enqueue(child.left)

    if child.right:
         queue.enqueue(child.right)

    child = queue.dequeue()
    








深度优先搜索, 使用栈实现

深度优先搜索使用[栈]来实现,遍历需要回溯用递归实现
1.遍历左子树
2.遍历右子树
3.遍历父节点

class Stack(object):
    
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def empty(self):
        return len(self.stack) == 0


        A
      /   \
     B     C
    /\     /\
   D   E  F  G

后序遍历：DEBFGCA

stack = Stack()

def dfs(child):
    ls = []
    stack.push(child)
    while not stack.empty():
        child = stack.pop()
        ls.insert(0 , child.data)

        if child.left:
            stack.push(child.left)

        if child.right:
            stack.push(child.right)

    return ls


dfs(root)




















# queue = Queue()
# queue.enqueue(root)

# child = queue.dequeue()
# while child:
#     print(child.data)
#     queue.enqueue(child.left)
#     queue.enqueue(child.right)
#     child = queue.dequeue()



# def dfs(child):
#     if child:
#         if child.left:
#             dfs(child.left)
#         if child.right:
#             dfs(child.right)
#         stack.push(child)

# dfs(root)


# while not stack.empty():
#     print(stack.pop().data)
