import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto("Hello Buddy", ("127.0.0.1", 42069))
