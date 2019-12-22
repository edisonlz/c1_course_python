#-*- coding:utf-8 -*-
import socket
import select
from queue import Queue


class ServerHandler(object):

    def __init__(self, ip="",port=6666, max_client_num=10):

        self.ip = ip
        self.port = port
        self.max_client_num = max_client_num
        self.serversocket = None
        self.timeout = 10
        self.epoll = None
        self.message_queues = {}
        self.fd_to_socket = {}
        self.server_fd = None

    def start(self):
        #创建socket对象
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #设置IP地址复用
        self.serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        #ip地址和端口号
        server_address = (self.ip, self.port)
        #绑定IP地址
        self.serversocket.bind(server_address)
        #监听，并设置最大连接数
        self.serversocket.listen(self.max_client_num)

        #服务端设置非阻塞
        self.serversocket.setblocking(False)  
        
        #创建epoll事件对象，后续要监控的事件添加到其中
        #int epoll_create(int size);
        self.epoll = select.epoll()

        #file_descriptor 文件描述符
        self.server_fd = self.serversocket.fileno()
        #注册服务器监听fd到等待读事件集合
        self.epoll.register(self.server_fd, select.EPOLLIN)

        #文件句柄到所对应对象的字典，格式为{句柄：对象}
        self.fd_to_socket = { self.server_fd : self.serversocket }


        print("服务器启动成功，监听IP:%s" , server_address)

        self.loop()

    def loop(self):        
        while True:
            print("等待连接......")
            #轮询注册的事件集合，返回值为[(文件句柄，对应的事件)，(...),....]
            #epoll.wait
            events = self.epoll.poll(self.timeout)

            if not events:
                print("epoll超时无活动连接，重新轮询......")
                continue

            for fd, event in events:
                socket = self.fd_to_socket[fd]
                #如果活动socket为当前服务器socket，表示有新连接
                if socket == self.serversocket:
                        connection, address = self.serversocket.accept()
                        print("新连接：%s" , address)
                        #新连接socket设置为非阻塞
                        connection.setblocking(False)
                        #注册新连接fd到待读事件集合
                        client_fd = connection.fileno()
                        self.epoll.register(client_fd, select.EPOLLIN)
                        #把新连接的文件句柄以及对象保存到字典
                        self.fd_to_socket[client_fd] = connection
                        #以新连接的对象为键值，值存储在队列中，保存每个连接的信息
                        self.message_queues[connection] = Queue()
                
                #读事件
                elif event & select.EPOLLIN:
                    #接收数据
                    data = socket.recv(1024)
                    if data:
                        print("发送 数据" ,socket.getpeername() , data )
                        #将数据放入对应客户端的字典
                        queue = self.message_queues[socket]
                        #收到什么发过去什么
                        queue.put(data)
                        #当前需要恢复，将客户端文件描述符，请切换到写事件
                        #int epoll_ctl(int epfd, int op, int fd, struct epoll_event *event);
                        self.epoll.modify(fd, select.EPOLLOUT)
                #写事件
                elif event & select.EPOLLOUT:
                    try:
                        #从字典中获取对应客户端的信息
                        queue = self.message_queues[socket]
                        #Queue.get(block=True, timeout=None)读出队列的一个元素，阻塞调用，无等待时间
                        msg = queue.get_nowait() #非阻塞
                    except Exception as e:
                        print(e)
                        self.epoll.modify(fd, select.EPOLLIN)
                    else :
                        print("发送数据" ,data,"客户端", socket.getpeername())
                        #发送数据，翻转数据
                        msg = msg[::-1]
                        socket.send(msg)
                        self.epoll.modify(fd, select.EPOLLIN)
            
                #关闭事件
                elif event & select.EPOLLHUP:
                    #hangup 挂断
                    print('client close')
                    #在epoll中注销客户端的文件句柄
                    self.epoll.unregister(fd)
                    #关闭客户端的文件句柄
                    connection = self.fd_to_socket[fd]
                    connection.close()
                    #在字典中删除与已关闭客户端相关的信息
                    del self.fd_to_socket[fd]
                    


    def close(self):
        #在epoll中注销服务端文件句柄
        self.epoll.unregister(self.server_fd)
        #关闭epoll
        self.epoll.close()
        #关闭服务器socket
        self.serversocket.close()



if __name__ == "__main__":
    ip = ""
    port = 6666
    server = ServerHandler(ip,port)
    server.start()
