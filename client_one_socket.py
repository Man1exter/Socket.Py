# FROM CLIENT v1

import socket as sc

HOST = '128.125.1.13'
PORT = 33

client_socket = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
# inet = ipv4 / inet6 = ipv6
client_socket.connect((HOST,PORT))