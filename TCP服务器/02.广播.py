from socket import *
udp_sokect = socket(AF_INET, SOCK_DGRAM)
#广播地址192.168.1.255和<broadcast>都可以
# send_address = "<broadcast>"
send_address = "192.168.2.255"
# 设置发送广播
# 第一个参数SOL_SOCKET是级别
# 第二参数操作:设置为广播
# 值
udp_sokect.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
while True:
    send_content = input("请你输入要发送的内容:")
    if not send_content:
        print("你输入的内容不能为空:")
        continue
    send_content = "1:12312312312:隔壁老王:老王-pc:32:%s" % send_content
    udp_sokect.sendto(send_content.encode("gb2312"), (send_address, 2425))
udp_sokect.close()