import socket

ip = "192.168.0.100"
port = 2419
lstnr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lstnr.sendto("accept".encode(), (ip, port))