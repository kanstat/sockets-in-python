import socket

host = "127.0.0.1"
port = 7000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host,port))
s.listen()

conn, addr = s.accept()
if conn:
    conn.send("Welcome to my Server\n".encode())
else:
    print("something went wrong while connect()")    
while True:
    to_send = input("YOU-> ")
    conn.send(to_send.encode())
    data_recvd = conn.recv(100).decode()
    if data_recvd == "exit":
        break
    print("CLIENT->",end='')        
    print(f"{data_recvd}")        




