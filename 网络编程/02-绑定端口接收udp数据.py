import socket


def main():
    # 创建udp套接字
    upd_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.bind绑定一个本地信息，以元组（"ip"地址，端口号）形式
    localaddr = ("", 7788)
    upd_socket.bind(localaddr)
    # 3.接受数据
    recv_data = upd_socket.recvfrom(1024)  # 1024表示接受的最大字节数
    # 4.打印收到的数据
    print(recv_data)
    # 5.关闭套接字
    upd_socket.close()


main()


