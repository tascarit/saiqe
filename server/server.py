import socket
import sys
sys.path.insert(0, "/home/tscrt/Desktop/saiqe")

import smtp

ip = "192.168.0.100"
port = 2417

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

listener.bind((ip, port))
listener.listen(0)

while True:
    conn, addr = listener.accept()

    msg = conn.recv(1024).decode()
    print(msg)

    if len(str(msg)) > 16 and len(str(msg)):

        uname, email, passw, local_ip = msg.split("|")
        print(email)

        answ = smtp.on_msg_send(email)

        conn.send(str(answ).encode())