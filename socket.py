# FROM SERVER

import socket as sc

HOST = '128.125.1.13'
PORT = 33000

server_socket = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
# inet = ipv4 / inet6 = ipv6
server_socket.bind((HOST,PORT))
