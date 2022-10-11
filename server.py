import socket

host = "127.0.0.1"
port = 5002

# createing a socket object

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

s.listen()

conn, addr = s.accept()
print(f"connected to client with {addr}")

conn.send("welcome to server".encode())

rec_data = conn.recv(1024).decode()
print(rec_data)
