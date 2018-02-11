import gevent
from gevent import monkey, socket
monkey.patch_all()

def recv_data(new_socket, new_address):
    while True:
        recv_content = new_socket.recv(1024)
        if len(recv_content) > 0:
                print("收到[%s]:%s" % (str(new_address), recv_content.decode("gb2312")))
                new_socket.send(recv_content)#发送到服务器上，服务器给反馈出来
        else:
            print("%s已经关闭" % (str(new_address)))
            new_socket.close()
            break


def main():
    s = socket.socket()
    s.bind(("", 8090))
    s.listen(5)
    while True:
        new_socket, new_address = s.accept()
        gevent.spawn(recv_data, new_socket, new_address)


if __name__ == "__main__":
    main()