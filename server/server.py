import socket
import smtp
import sys
sys.path.insert(0, "/home/tscrt/Desktop/saiqe/db_users/")
import db_func
import hash_token

ip = "localhost"
port = 2417

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

listener.bind((ip, port))
listener.listen(0)

while True:
    conn, addr = listener.accept()

    msg = conn.recv(1024).decode()


    if "111111?" in str(msg):

        xf = str(msg)[7:]
        answ = db_func.on_token_find(xf)

        conn.send(str(answ).encode())

    elif "|" in str(msg):

        uname, email, passw, local_ip = msg.split("|")
        res = smtp.on_msg_send(email)
        conn.send(res.encode())

    elif "encrypt?" in str(msg):
        xf = hash_token.on_encrypt(str(msg)[8:])

        conn.send(xf.encode())

    elif "decrypt?" in str(msg):
        token = hash_token.on_decrypt(str(msg)[8:])

        conn.send(token.encode())

    elif "get_avatar?" in str(msg):
        avatar_id = db_func.on_avatar_find(str(msg[11:]))

        conn.send(str(avatar_id).encode())

    else:
        
        name = str(msg)
        email = db_func.on_email_find(name)
        res = smtp.on_ip_verify(email)
        conn.send(res.encode())

