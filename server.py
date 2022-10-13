import socket
import threading


def check_mssgs_from_client(conn):
    while True:
        data_recv = conn.recv(1024).decode()
        if data_recv == "exit":
            break
        print("CLIENT->", end="")
        print(data_recv)


host = "127.0.0.1"
port = 7000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
s.listen()

conn, addr = s.accept()
if conn:
    conn.send("Welcome to my Server\n".encode())
    st = threading.Thread(target=check_mssgs_from_client, args=(conn,))
    st.start()
else:
    print("something went wrong while connect()")


while True:
    to_send = input("YOU(Server)-> ")
    conn.send(to_send.encode())
