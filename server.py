# import socket module
import socket
import threading

# function to handle the received data from the client continuously
def client_ne_kuch_bheja_kya(connected_client,nickname):
    while True:
        try:
            client_ka_bheja_hua_mssg = connected_client.recv(1024).decode()
            print("\33[2K",end="")
            # print("\r"+client_ka_bheja_hua_mssg+"\nSERVER:",end=" ")
            if client_ka_bheja_hua_mssg == "exit!!":
                print(f"{nickname} has closed the connection !!")
                break
            print(f"\r{nickname}: {client_ka_bheja_hua_mssg}\nSERVER:",end=" ")
        except:
            break
<<<<<<< HEAD
        print("CLIENT->", end="")
        print(data_recv)


host = "127.0.0.1"
port = 7000
=======
>>>>>>> 8976bac99066072259ed322280bc03b931055c9e

# # creating a object of socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

<<<<<<< HEAD
s.bind((host, port))
=======
server_host = "127.0.0.1"
server_port = 2005

s.bind((server_host, server_port)) 

>>>>>>> 8976bac99066072259ed322280bc03b931055c9e
s.listen()
client_nickname = None
print(f"SERVER is running at {server_host} on port {server_port}\n")
conn, addr = s.accept()
<<<<<<< HEAD
if conn:
    conn.send("Welcome to my Server\n".encode())
    st = threading.Thread(target=check_mssgs_from_client, args=(conn,))
    st.start()
else:
    print("something went wrong while connect()")


while True:
    to_send = input("YOU(Server)-> ")
    conn.send(to_send.encode())
=======
client_nickname = conn.recv(1024).decode()
if client_nickname:
    print(f"{client_nickname} has joined the server.")
conn.send(f"Hello {client_nickname}, Welcome to the server\n".encode())
conn.send("You can send your texts now...\n".encode())
# Thread to handling receiving mssgs from client independently
client_thread = threading.Thread(target=client_ne_kuch_bheja_kya, args=(conn,client_nickname))
client_thread.start()

while True:
    d = input("\rSERVER: ")
    if d != "exit!!" or not conn:
        conn.send(d.encode())
    else:
        print("Closing the Server because of no client")
        conn.close()
        break
>>>>>>> 8976bac99066072259ed322280bc03b931055c9e
