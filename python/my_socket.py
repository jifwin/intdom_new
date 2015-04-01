import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 9090))
s.sendall("dupa2")
s.close()
