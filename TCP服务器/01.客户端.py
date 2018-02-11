from socket import AF_INET, SOCK_STREAM, socket
#创建套接字
tcp_client = socket(AF_INET, SOCK_STREAM)
#发送链接到服务器（ip和端口）
tcp_client.connect(("192.168.28.23", 7788))
#tcp_address = (('192.168.28.23',8080))
#服务器接受
send_socket = input('请输入需要发送的消息:')
tcp_client.send(send_socket.encode('gb2312'))
recv_data = tcp_client.recv(1024)
#解码
print(recv_data.decode('gb2312'))
tcp_client.close()


