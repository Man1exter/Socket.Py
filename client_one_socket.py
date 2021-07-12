# FROM CLIENT v1

import socket as sc

HOST = '192.168.8.122'
PORT = 33

client_socket = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
# inet = ipv4 / inet6 = ipv6
client_socket.connect((HOST,PORT))

name = input("Name: ").encode("utf8")
s_name = input("Second Name: ").encode("utf8")

client_socket.send(name)
client_socket.send(s_name)