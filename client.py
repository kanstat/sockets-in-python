import socket
import threading

def check_mssgs_from_server(conn):
    while True:
        data_recv = conn.recv(1024).decode()
        print("SERVER->",end="")
        print(data_recv)


if __name__ == "__main__":
    server_host = "127.0.0.1"
    server_port = 7000

    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((server_host,server_port))        
    if c:
        recv_thread = threading.Thread(target=check_mssgs_from_server,args=(c,))
        recv_thread.start()
    while True:
        to_send = input("YOU->")
        c.send(to_send.encode())