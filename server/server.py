import socket
import smtp
import sys
sys.path.insert(0, "/home/tscrt/Desktop/saiqe/db_users/")
import db_func

ip = "192.168.0.112"
port = 2417

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

listener.bind((ip, port))
listener.listen(0)

while True:
    conn, addr = listener.accept()

    msg = conn.recv(1024).decode()

    if len(str(msg)) > 24:

        if "|" in str(msg):

            uname, email, passw, local_ip = msg.split("|")
            res = smtp.on_msg_send(email)
            conn.send(res.encode())

    else:
        
        name = str(msg)
        email = db_func.on_email_find(name)
        res = smtp.on_ip_verify(email)
        conn.send(res.encode())

