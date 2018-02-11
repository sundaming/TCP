from socket import *
from select import select
def main():
    #创建服务器
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind(('', 1245))
    server_socket.listen(5)
    #客户端列表
    socket_lists = [server_socket]
    try:
       while True:
           #
           readable, writeable, excep = select(socket_lists, [], [])
           for sock in readable:
               if sock == server_socket:
                   print(sock ==server_socket)
                   new_socket,new_address = sock.accept()
                   socket_lists.append(new_socket)
               else:
                   recv_data = sock.recv(1024)
                   if len(recv_data) > 0:
                       print("从[%s]发过消息:%s" % (str(new_address), recv_data.decode('gb2312')))
                       sock.send(recv_data)
                   else:
                       print("客户端已经断开链接")
                       sock.close()
                       socket_lists.remove(sock)

    finally:
        server_socket.close()

if __name__ == '__main__':
    main()
