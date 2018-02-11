from socket import socket,AF_INET,SOCK_STREAM,SO_REUSEADDR,SOL_SOCKET
socket_lists = []
def main():
    server_tcp = socket(AF_INET, SOCK_STREAM)
    server_tcp.bind(("", 8888))
    server_tcp.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_tcp.setblocking(False)
    server_tcp.listen(5)
try:
    while True:
        try:
            new_socket,new_address = server_tcp.accept()#非阻塞的
            pass
        except Exception as resul:
            pass
        else:
            new_socket.setblocking(False)
            socket_lists.append((new_socket, new_address))
            print("有新的客户端链接:%s" % str(new_address))
        for sock,address in socket_lists:
            try:
                recv_data = sock.recv(1024)
                print("recv_data--222")
            except Exception as resul:
                pass
            else:
                if len(recv_data) > 0:
                    print("%s:%s" % (str(address), recv_data.decode("gb2312")))
                    sock.send("thank you!".encode("gb2312"))
                else:
                    print("%s已经掉线" % str(address))
                    sock.close()
                    socket_lists.remove((sock, address))
                    break
finally:
    #server_tcp.close()
    print("关闭最外面的套接字..")

if __name__ == "__main__":
    main()
