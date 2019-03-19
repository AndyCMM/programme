# coding=utf-8
# @Time  :2019-03-11 12:30
# @Author:AndyMing
# @File  :多任务udpclien.py

from socket import *
import threading


# ADDR = ('172.22.122.98', 8091)


# while True:
#     data = input('pleasr input data:')
#     if not data:
#     	break
#     udp.sendto(data.encode(), ADDR)
#     rece_data, addr = udp.recvfrom(1024)
#     print(addr,':', end='')
#     print(rece_data.decode())
# udp.close()


def recmsg(udp):
    while True:
        data, addr = udp.recvfrom(1024)
        if not data:
            break
        print(addr, ':', data.decode())


def sendmsg(udp, addr):
    while True:
        data = input('me:')
        if not data:
            break
        udp.sendto(data.encode(), addr)


def communicate(udp, addr):
    thread = []
    thread.append(threading.Thread(target=sendmsg, args=(udp, addr)))
    thread.append(threading.Thread(target=recmsg, args=(udp,)))
    for i in range(len(thread)):
        print('thread start')
        thread[i].start()
    for i in range(len(thread)):
        thread[i].join()
    print('communicate finish!')


def main():
    while True:
        ip = input('please input IP address:')
        port = int(input('please input port:'))
        ADDR = (ip, port)
        udp = socket(AF_INET, SOCK_DGRAM)
        communicate(udp, ADDR)
        if input('finish?') == 'yes':
            break


if __name__ == '__main__':
    main()
