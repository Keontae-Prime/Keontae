#Keontae Trotman
#This program creates a server that clients can connect to.
import socket
import threading
HEADER=64
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)FORMAT='utf-8'

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected=True
    while connected:
        msg_length=conn.recv(HEADER).decode(FORMAT)
        msg_length=int(msg_length)
        msg=conn.recv(HEADER).decode(FORMAT)
        print(f"[{addr}] {msg}")
def start():
    server.listen()
    while True:
        conn, addr=server.accept()
        thread = threading/threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS{threading.activeCount()-1}")
print("[STARTING] server is starting...")
start()
#Stopped at 30 min mark