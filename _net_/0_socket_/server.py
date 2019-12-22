#coding=utf-8
import socket


def echo_server(address, backlog=5): 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.bind(address)
    sock.listen(backlog)
    
    print("[server on] ip:%s ,port:%s" % address)

    while True:
        #非阻塞与阻塞
        client_sock, client_addr = sock.accept()

        print("client on", client_addr)
        #123   ----  321
        #client --- server 
        msg = client_sock.recv(8192)
        msg = msg[::-1] #消息翻转
        print("msg:%s" % msg)
        client_sock.sendall(msg)
        

if __name__ == '__main__': 
    ip = ''
    port = 20000
    echo_server((ip, port))

