#coding=utf-8

#网络编程的应用 HTTP 

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
        url_path = client_sock.recv(8192)
        print(url_path)
        data = b""
        if url_path  == b"/home":
            data = b"""
            <html>
                <head><head>
                <body>
                    hello world!
                <body>
            </html>
            """
            
     
        print("return :%s" % data)
        client_sock.sendall(data)
        

if __name__ == '__main__': 
    ip = ''
    port = 8080
    echo_server((ip, port))

