from socket import *
tcp_socket = socket(AF_INET,SOCK_STREAM)
tcp_socket.bind(("", 8989))
tcp_socket.listen(3)
while True:
    #有新的客户端连接,返回新的socket和地址
    new_sokect ,new_address = tcp_socket.accept()
    #发消息给客户端--链接好了
    new_sokect.send("我是服务端,我发数据给你了哦".encode("gb2312"))
    recv_data = new_sokect.recv(1024)#如果链接的另外一段,端口后,解除阻塞
#关闭套接字
new_sokect.close()
tcp_socket.close()
