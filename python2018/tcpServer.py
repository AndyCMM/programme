import socket


ip = ''
port = 8991
tcps = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcps.bind((ip, port))
tcps.listen(2)
print('wait')
con, addr = tcps.accept()
print('connect')
data = con.recv(1024)
print(addr, data.decode())
con.send('copy that!'.encode())
con.close()
tcps.close()
