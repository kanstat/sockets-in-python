import socket


server_host = "127.0.0.1"
server_port = 7000

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c.connect((server_host,server_port))
data_recv = c.recv(100).decode()
print("SERVER->",end="")
print(data_recv)
while True:
    to_send = input("YOU->")
    c.send(to_send.encode())
    data_recv = c.recv(100).decode()
    print("SERVER->",end="")
    print(data_recv)