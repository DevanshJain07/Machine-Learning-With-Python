import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto(b"Hello from client",('127.0.0.1',12346))
print(s.recvfrom(2048))



