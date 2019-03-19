import socket


def main():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip = input('please input IP:')
    port = int(input('please input port:'))
    # tcp.bind(('localhost', 8989))
    ip = ''
    port = 8989
    tcp.connect((ip, port))
    send_data = input(':')
    tcp.send(send_data.encode())
    tcp.close()


if __name__ == "__main__":
    main()
