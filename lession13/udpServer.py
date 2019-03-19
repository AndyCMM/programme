# coding=utf-8
# @Time  :2019-03-10 16:28
# @Author:AndyMing
# @File  :udpServer.py

from socket import *

ADDR = ('', 8989)
udp = socket(AF_INET, SOCK_DGRAM)
udp.bind(ADDR)


def communicate(udp, addr):
    pass

def
while True:
    # print('I am waiting!')
    data, addr = udp.recvfrom(1024)
    if data.decode() == '11':
        communicate(udp, addr)
    print('communicate finish!')
udp.close()

