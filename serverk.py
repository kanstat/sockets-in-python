# import socket module

import socket

# # creating a object of socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 2005

s.bind((host, port))

s.listen()

conn, adrr = s.accept()
conn.send(f"welcome to server {adrr}\n".encode())

while True:

    conn.send("Hey type something...".encode())

    d = conn.recv(1024).decode()
    print(d)

    d = input("Write a reply to the client--->>")
    conn.send(d.encode())

############################################################################

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print(f"Connected by {addr}")
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             conn.sendall(data)
