import socket

lstnr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lstnr.connect(("192.168.0.100", 5000))

lstnr.send("e".encode())
lstnr.close()