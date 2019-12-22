网络编程

一，什么是TCP/IP协议？
是指能够在多个不同网络间实现信息传输的协议簇。


TCP协议两个要点：
TCP三次握手 - 建立连接
TCP四次挥手 - 断开连接


二，什么是socket？
 socket “套接字”，它是计算机之间进行通信的一种约定。


1.创建客户端socket对象

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    socket.AF_INET  -- IPV4
    socket.AF_INET6 -- IPV6

    socket.SOCK_STREAM -- TCP 流式socket *
    socket.SOCK_DGRAM -- UDP 数据报式socket



2.设置IP地址复用
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    socket.SOL_SOCKET 套接字层选项

    socket.SO_REUSEADDR 
    允许启动一个监听服务器并捆绑其众所周知端口，
    【即使】以前建立的将此端口用做他们的本地端口的连接仍存在。

    socket.SO_REUSEADDR
    允许在同一端口上启动同一服务器的多个实例


3. int listen(int sockfd, int backlog)
    sockfd 服务器端的文件描述符
    backlog是一个建议值，用于指定内部的队列大小，以控制同时建立的连接请求数量

4. sock.bind(address) 服务器监听