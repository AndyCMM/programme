# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 23:54:44 2019

@author: Andy
"""

from socket import *
import threading


def communicate(udp, addr):
    loop = []
    loop.append(threading.Thread(target=sendmsg, args=(udp, addr)))
    loop.append(threading.Thread(target=recmsg, args=(udp,)))
    for i in range(len(loop)):
        print('loop start')
        loop[i].start()
    for i in range(len(loop)):
        loop[i].join()
    print('jieshu')


def sendmsg(udp, adddr):
    print('dsads')
    while True:
        print(addr, end='')
        data = input(' please input:')
        if not data:
            break
        udp.sendto(data.encode(), addr)
    print('不聊了')


def recmsg(udp):
    while True:
        data, addr = udp.recvfrom(1024)
        if data.decode() == 'bye':
            break
        print(addr, ' send msg:', data.decode())
    print('对方已下线')


ADDR = ('', 8091)
udpserver = socket(AF_INET, SOCK_DGRAM)
udpserver.bind(ADDR)
while True:
    print('wait for connect')
    if input() == 'exit':
        break
    data, addr = udpserver.recvfrom(1024)
    print(data.decode(), addr)
    if data.decode() == '1':
        communicate(udpserver, addr)
    print('connect finish!')
    
udpserver.close()
