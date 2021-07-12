# FROM SERVER

import socket as sc

HOST = 'hide'
PORT = 33000

BUFFER = 1024

server_socket = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
# inet = ipv4 / inet6 = ipv6

server_socket.bind((HOST,PORT))
server_socket.listen(2)
# 2/3 listen ,,channel,,?

while True:  
     client_socket, address = server_socket.accept()

     name, id_name = client_socket.recv(BUFFER).decode("utf8")

     print(f"Connect from => {address[0]}:{address[1]}")
     print(f"ABOUT CONNECTING PERSON => {name}:{id_name}")

     greeting = "HELLLLLLLOOOOOOOO".encode("utf8")
     client_socket.send(greeting)
	