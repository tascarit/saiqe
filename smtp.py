import smtplib
import socket
import random
import PIL
from PIL import Image
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def on_msg_send():

    verification_code = random.randint(100000, 999999)

    domain = 'saiqe@internet.ru'
    email = "assler.15@yandex.ru"

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Подтверждение почты | Saiqe"
    msg["From"] = domain
    msg["To"] = email
    print("sus")
    msg.preamble = "Your verification code {}".format(str(verification_code))
    print("s")

    with open("")

    smtp = smtplib.SMTP(host="smtp.mail.ru", port=25)
    smtp.starttls()
    print("s")
    try:
        smtp.login("saiqe@internet.ru", "qPyC9340bcaWym041PQr")
        print("suuuu")
        smtp.sendmail(domain, email, msg.as_string())
        print("success")

        return "success" + "|" + str(verification_code)
    
    except Exception as e:
        print(e)
        return "error"
    
    finally:
        smtp.quit()

on_msg_send()