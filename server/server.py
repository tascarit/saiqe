import socket
import smtp

ip = "192.168.0.102"
port = 2417

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

listener.bind((ip, port))
listener.listen(0)

while True:
    conn, addr = listener.accept()

    msg = conn.recv(1024).decode()

    if len(str(msg)) > 16:

        uname, email, passw, local_ip = msg.split("|")

        res = smtp.on_msg_send(email)

        conn.send(res.encode())

