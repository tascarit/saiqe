import socket
import smtp
import sys
sys.path.insert(0, "/home/tscrt/Desktop/saiqe/db_users/")
import db_func
import hash_token
from PIL import ImageTk, Image, ImageDraw, ImageOps
import random

ip = "localhost"
port = 2417

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

listener.bind((ip, port))
listener.listen(0)

while True:
    conn, addr = listener.accept()

    msg = conn.recv(1024).decode()

    if "111111?" in msg:

        xf = msg[7:]
        answ = db_func.on_token_find(xf)

        conn.send(str(answ).encode())

    elif "|" in msg:

        uname, email, passw, local_ip = msg.split("|")
        res = smtp.on_msg_send(email)
        conn.send(res.encode())

    elif "encrypt?" in msg:
        xf = hash_token.on_encrypt(msg[8:])

        conn.send(xf.encode())

    elif "decrypt?" in msg:
        token = hash_token.on_decrypt(msg[8:])

        conn.send(token.encode())

    elif "get_avatar?" in msg:
        avatar_id = db_func.on_avatar_find(msg[11:])
        file = open("/home/tscrt/Desktop/saiqe/db_users/pfps/{}.png".format(avatar_id), "rb")

        while True:
            file_data = file.read(1024)
            conn.send(file_data)
            if not file_data:
                break

        conn.close()


    elif "get_c_picture?" in msg:
        file = open("/home/tscrt/Desktop/saiqe/images/cancel.png", "rb")

        while True:
            file_data = file.read(1024)
            conn.send(file_data)
            if not file_data:
                break

        conn.close()

    elif "get_r_picture?" in msg:
        file = open("/home/tscrt/Desktop/saiqe/images/refresh.png", "rb")

        while True:
            file_data = file.read(1024)
            conn.send(file_data)
            if not file_data:
                break

        conn.close()

    elif "get_icon?" in msg:
        file = open("/home/tscrt/Desktop/saiqe/icon.png", "rb")

        while True:
            file_data = file.read(1024)
            conn.send(file_data)
            if not file_data:
                break

        conn.close()

    elif "get_bg?" in msg:
        file = open("/home/tscrt/Desktop/saiqe/bg.png", "rb")

        while True:
            file_data = file.read(1024)
            conn.send(file_data)
            if not file_data:
                break

        conn.close()

    elif "get_settings_button?" in msg:
        file = open("/home/tscrt/Desktop/saiqe/images/settings.png", "rb")

        while True:
            file_data = file.read(1024)
            conn.send(file_data)
            if not file_data:
                break

        conn.close()

    elif "change_avatar?" in msg:
            
            index, name = msg.split("?")
            avatar_id = random.randint(10000000000000000, 999999999999999999999999)
            file = open("/home/tscrt/Desktop/saiqe/db_users/pfps/{}.png".format(str(avatar_id)), "w+b")

            conn.send("accept".encode())
            while True:
                data = conn.recv(10485769)
                file.write(data)
                if not data:
                    file.close()
                    break
            conn.close()

            mask = Image.new('L', (65, 65), 0)
            draw = ImageDraw.Draw(mask) 
            draw.ellipse((0, 0) + (65, 65), fill=255)

            Img = Image.open("/home/tscrt/Desktop/saiqe/db_users/pfps/{}.png".format(str(avatar_id)))

            output = ImageOps.fit(Img, mask.size, centering=(0.5, 0.5))
            output.putalpha(mask)
            output.thumbnail((65, 65), Image.ANTIALIAS)
            output.save("/home/tscrt/Desktop/saiqe/db_users/pfps/{}.png".format(str(avatar_id)))
            mask.close()

            db_func.on_avatar_add(str(avatar_id), name)

    elif "check_name_exists?" in msg:
        name = msg[17:]
        answ = db_func.on_acc_check(name)
        conn.send(answ.encode())


    else:
        
        name = msg
        email = db_func.on_email_find(name)
        res = smtp.on_ip_verify(email)
        conn.send(res.encode())

