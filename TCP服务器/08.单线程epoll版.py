from  socket import socket,AF_INET,SO_REUSEADDR,SOCK_STREAM,SOL_SOCKET
import select
def main():
	#创建套接字
	server = socket(AF_INET,SOCK_STREAM)
	#绑定端口
	server.bind(("",9999))
	#设置端口可以重用
	server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
	#设置监听
	server.listen(5)
	#得到epoll
	epoll = select.epoll()#类->实例对象
	#注册监听sockect
	#第一个参数是:要监听的socket的文件描述符
	#第二参数:要监听接收数据和立刻通知
	epoll.register(server.fileno(),select.EPOLLIN|select.EPOLLET)
	print(server.fileno())
	socket_lists = {}
	address_lists = {}
	try:
		while True:
			#如果有新的客户端和可以收数据的socket和断开的socket就解除阻塞
			print("epoll.poll()--1111")
			#[(3, 1)]
			epoll_list = epoll.poll()
			print("epoll.poll()--222")
			print(epoll_list)
			for fd,event in epoll_list:
				#当前的文件描述符,是3,就是server
				if fd == server.fileno():
					#有新的客户端链接了
					new_socket,new_address = server.accept()
					# 当有新的链接就会创建新的sockect,但是也要注册到epoll中
					epoll.register(new_socket.fileno(), select.EPOLLIN | select.EPOLLET)
					socket_lists[new_socket.fileno()] = new_socket
					address_lists[new_socket.fileno()] = new_address
					print("有客户端[%s]链接进来了" % str(new_address))
				#当有客户端的数据发送过来的时候
				elif event == select.EPOLLIN:
					# new_socket和客户端进行交互数据了
					new_socket = socket_lists[fd]
					new_address = address_lists[fd]
					recv_data = new_socket.recv(1024)#长度0
					if len(recv_data) > 0:
						print("已经收到[%s]:%s" % (str(new_address),recv_data.decode("gb2312")))
						new_socket.send(recv_data)#客户端发什么数据给服务器,服务器就发什么给客户端
					else:
						print("[%s]已经客户端已经关闭" % (str(new_address)))
						new_socket.close()
	finally:
		print("关闭最外面的socket")
		#关闭套接字
		server.close()


main()