import socket


def main():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # ip = input('please input IP:')
    # port = int(input('please input port:'))
    # tcp.bind(('localhost', 8989))
    ip = 'localhost'
    port = 8991
    tcp.bind(('', 9001))
    tcp.connect((ip, port))
    send_data = input(':')
    tcp.send(send_data.encode())
    data = tcp.recv(1024)
    print(data)
    tcp.close()


if __name__ == "__main__":
    main()
