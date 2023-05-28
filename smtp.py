import smtplib
import socket
import random
import PIL
import os
from PIL import Image, ImageDraw, ImageFont
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def on_img_create(email):

    verification_code = random.randint(100000, 999999)
    random_nums = str(random.randint(100000000000000000000, 999999999999999999999999999999999999))

    email_verify_img = Image.open("/home/tscrt/Desktop/saiqe/email.png")
    draw_text = ImageDraw.Draw(email_verify_img)
    font = ImageFont.truetype("/home/tscrt/Desktop/saiqe/Jura.ttf", 180)
    draw_text.text((134, 337), str(verification_code), fill="#000000", font=font)

    email_verify_img.save("/home/tscrt/Desktop/saiqe/email_{}.png".format(random_nums))

    on_msg_send(verification_code, "/home/tscrt/Desktop/saiqe/email_{}.png".format(random_nums), email)

def on_msg_send(verification_code, img_path, email):

    domain = 'saiqe@internet.ru'

    msg = MIMEMultipart()
    msg["Subject"] = "Подтверждение почты | Saiqe"
    msg["From"] = domain
    msg["To"] = email

    msgText = MIMEText('<b></b><br><img src="cid:%s"><br>' % (img_path), 'html')
    msg.attach(msgText)

    img_raw = open(str(img_path), "rb").read()
    img = MIMEImage(img_raw, "png")
    img.add_header('Content-ID', '<{}>'.format(img_path))

    msg.attach(img) 

    smtp = smtplib.SMTP(host="smtp.mail.ru", port=25)
    smtp.starttls()
    try:
        smtp.login("saiqe@internet.ru", "qPyC9340bcaWym041PQr")
        smtp.sendmail(domain, email, msg.as_string())

        return "success" + "|" + str(verification_code)
    
    except Exception as e:
        return "error"
    
    finally:
        os.remove(img_path)
        smtp.quit()

on_img_create()