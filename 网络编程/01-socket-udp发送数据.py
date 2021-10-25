import socket


def main():
    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 使用套接字发送数据
    # udp_socket.sendto("发送的数据"是字节类型，对方的ip以及端口用元组表示)
    udp_socket.sendto(b"hahhah", ("192.168.33.5", 8080))

    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()