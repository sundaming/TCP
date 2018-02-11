from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
def send_msg(new_socket):
    while True:
        send_data = input('服务器发送的消息:')
        new_socket.send(send_data.encode('gb2312'))
def recv_msg(new_socket, new_address):
    while True:
        recv_data = new_socket.recv(1024)
        if len(recv_data) == 0:
            print("%s已经断开链接" % str(new_address))
            break
        print('接受的消息:%s' % recv_data.decode('gb2312'))
def main():

    tcp_server = socket(AF_INET, SOCK_STREAM)
    tcp_server.bind(('', 2529))
    tcp_server.listen(5)
    while True:
        new_socket, new_address = tcp_server.accept()
        Thread(target=recv_msg, args=(new_socket, new_address)).start()
        Thread(target=send_msg, args=(new_socket,)).start()
    tcp_server.close()
    new_socket.close()
if __name__ == '__main__':
    main()


