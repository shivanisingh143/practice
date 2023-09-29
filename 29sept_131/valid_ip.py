import socket

st = '127000.0.0.100'
try:
    socket.inet_aton(st)
    print('valid ip')
except Exception as e:
    print(e)