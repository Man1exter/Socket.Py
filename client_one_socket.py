# FROM CLIENT v1

from server_socket import BUFFER
import socket as sc

HOST = '192.168.8.122'
PORT = 3300

BUFFER = 1024

client_socket = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
# inet = ipv4 / inet6 = ipv6
client_socket.connect((HOST,PORT))

name = input("Name: ").encode("utf8")
id_name = input("Second Name: ").encode("utf8")

client_socket.send(name)
client_socket.send(id_name)

msg = client_socket.recv(BUFFER).decode("utf8")
print("Server> "+msg)