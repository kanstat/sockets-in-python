# import socket module
import socket
import threading

<<<<<<< HEAD

def check_mssgs_from_server(conn):
    while True:
        data_recv = conn.recv(1024).decode()
        print("SERVER->", end="")
        print(data_recv)
=======
# function to handle the received data from the client continuously
def server_ne_kuch_bheja_kya(connected_server,nickname):
    while True:
        if connected_server:
            try:
                server_ka_bheja_hua_mssg = connected_server.recv(1024).decode()
                print("\33[2K",end="")
                # print("\r"+nickname+":"+server_ka_bheja_hua_mssg+"\nCLIENT:",end=" ")
                print(f"\rSERVER: {server_ka_bheja_hua_mssg}\nCLIENT:",end=" ")
            except:
                break
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
>>>>>>> 8976bac99066072259ed322280bc03b931055c9e

server_host_to_be_connected = "127.0.0.1"
server_port_to_be_connected = 2005

c.connect((server_host_to_be_connected, server_port_to_be_connected))
nickname = input("Enter your chat-room name: ")
if nickname:
    c.send(f"{nickname}".encode())
else:
    c.send(f"CLIENT".encode())
    
# Thread to handling receiving mssgs from client independently
server_thread = threading.Thread(target=server_ne_kuch_bheja_kya, args=(c,nickname))
server_thread.start()

<<<<<<< HEAD
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((server_host, server_port))
    if c:
        recv_thread = threading.Thread(
            target=check_mssgs_from_server, args=(c,))
        recv_thread.start()
    while True:
        to_send = input("YOU->")
        c.send(to_send.encode())
=======
while True:
    mssg_to_send = input("\rCLIENT: ")
    if mssg_to_send != "exit!!":
        c.send(f"{mssg_to_send}".encode())
    else:
        c.close()
        break
>>>>>>> 8976bac99066072259ed322280bc03b931055c9e
