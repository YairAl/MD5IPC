import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
START_MESSAGE = "!START"
CONNECTION_NUMBER = 0

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

connections = []


def broadcast():
    for i in range(len(connections)):
        end_num = (i + 1) * 9999999999 / len(connections) - 1
        start_num = i * 9999999999 / len(connections)
        print(start_num, end_num)
        connections[i].send(f"{start_num}, {end_num}".encode(FORMAT))
        print("sent")


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:  # receive message from this client
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            elif msg == START_MESSAGE:
                broadcast()
    conn.close()


def start():
    global CONNECTION_NUMBER
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        print(f"New Connection: {conn}\n{addr}")
        connections.append(conn)
        CONNECTION_NUMBER += 1
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()
