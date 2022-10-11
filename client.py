import socket

host = "127.0.0.1"
port = 5002

# createing a socket object

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c.connect((host, port))

print("connected to server")

to_send = input("type your msh here--->>")

c.send(to_send.encode())
# c.recv(1024).decode()
