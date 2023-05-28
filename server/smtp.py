import smtplib
import random
import os
from PIL import Image, ImageDraw, ImageFont
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

ip = "192.168.0.102"
port = 2417


def on_msg_send(email):

    verification_code = random.randint(100000, 999999)
    random_nums = str(random.randint(100000000000000000000, 999999999999999999999999999999999999))

    email_verify_img = Image.open("/home/tscrt/Desktop/saiqe/email.png")
    draw_text = ImageDraw.Draw(email_verify_img)
    font = ImageFont.truetype("/home/tscrt/Desktop/saiqe/Jura.ttf", 180)
    draw_text.text((134, 337), str(verification_code), fill="#000000", font=font)

    email_verify_img.save("/home/tscrt/Desktop/saiqe/email_{}.png".format(random_nums))

    domain = 'saiqe@internet.ru'
    img_path = "/home/tscrt/Desktop/saiqe/email_{}.png".format(random_nums)

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

        res = "success" + "|" + str(verification_code)

        return res
    
    except Exception as e:
        return "error"
    
    finally:
        os.remove(img_path)
        smtp.quit()