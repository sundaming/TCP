from socket import *
from threading import Thread
def send_info(tcp_socket):
   while True:
      send_content = input("请输入内容：")
      tcp_socket.send(send_content.encode("gb2312"))
def recv_info(tcp_socket,tcp_address):
   while True:
      recv_tcp = tcp_socket.recv(1024)
      if len(recv_tcp) == 0:
         break
      print("来自%s:%s" % (tcp_address, recv_tcp.decode("gb2312")))
def main():
   tcp_socket = socket(AF_INET, SOCK_STREAM)
   tcp_address = ("192.168.28.29", 8080)
   tcp_socket.connect(tcp_address)
   Thread(target=send_info,args=(tcp_socket,)).start()
   Thread(target=recv_info,args=(tcp_socket,tcp_address)).start()
if __name__ == "__main__":
   main()