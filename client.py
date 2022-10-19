import socket
from MD5 import *

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


def recv():
    msg = client.recv(2048).decode(FORMAT)
    start_num = msg.split(',')[0]
    end_num = msg.split(',')[1]
    md5hash = msg.split(',')[2]
    print("start num: ", start_num, "end num: ", end_num)
    thread = threading.Thread(target=MD5, args=(start_num, end_num, md5hash))
    thread.start()


def main():
    while True:
        receive = threading.Thread(target=recv)
        receive.start()
        msg = input("Would You Like To Begin?: (Y/N) ")
        if msg == "Y":
            send("!START")


# send(DISCONNECT_MESSAGE)

if __name__ == '__main__':
    main()
