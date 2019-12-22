#-*- coding:utf-8 -*-

import socket



#创建客户端socket对象
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#服务端IP地址和端口号元组
server_address = ('127.0.0.1',8080)
#客户端连接指定的IP地址和端口号
client_socket.connect(server_address)

while True:
    #输入数据
    data = str(input('please input:'))
    #客户端发送数据
    client_socket.sendall(data.encode())
    #客户端接收数据
    server_data = client_socket.recv(1024)
    print('客户端收到的数据：%s' % server_data)
    

