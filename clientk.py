# import socket module
import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 2005

c.connect((host, port))
while True:
    rec = c.recv(1024).decode()
    print(rec)

    d = input("Write something to send it to server---->>")
    c.send(f"{d}".encode())

######################################################################
# import socket

# HOST = "127.0.0.1"  # The server's hostname or IP address
# PORT = 2005  # The port used by the server

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     s.sendall(b"Hello, world")
#     data = s.recv(1024)

# print(f"Received {data!r}")
