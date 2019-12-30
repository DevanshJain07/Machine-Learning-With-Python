import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('127.0.0.1',12345))
#print(s.recv(2048))
msg=s.recv(2048)
print(msg.decode())
if msg.decode()=="Hello":
    s.send(b"Hi")
s.close()


