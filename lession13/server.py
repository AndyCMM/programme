# coding=utf-8
# @Time  :2019-03-09 23:39
# @Author:AndyMing
# @File  :server.py

from socket import *
from time import ctime, clock

HOST = "localhost"
POST = 21567
buf_size = 1024
ADDR = (HOST, POST)
ser = socket(AF_INET, SOCK_STREAM)
ser.connect(ADDR)
while True:
    data = input('>>')
    data = data.encode(encoding='utf-8')
    print(type(data), data)
    if not data:
        break
    ser.send(data)
    data = ser.recv(buf_size)
    if not data:
        break
    print(data.decode())
ser.close()