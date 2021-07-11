# FROM CLIENT v2

import socket as sc

HOST = '128.125.1.14'
PORT = 33001

server_socket = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
# inet = ipv4 / inet6 = ipv6