# coding=utf-8
# @Time  :2019-03-09 23:02
# @Author:AndyMing
# @File  :client.py

from socket import *
from time import ctime
HOST = ''
POST = 21567
ADDR = (HOST, POST)
cl = socket(AF_INET, SOCK_STREAM)
cl.bind(ADDR)
cl.listen(5)
buf_size = 1024
while True:
    print('wait for connect')
    tcp, addr = cl.accept()
    print('bulit connect', addr)
    while True:
        data = tcp.recv(buf_size)
        if not data:
            break

        a = '[%s]: [%s]' % (ctime(), data)
        print(a)
        tcp.send(a.encode())
    tcp.close()
cl.close()
