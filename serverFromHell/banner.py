#!/usr/bin/python3

import socket

IP = "10.10.128.89"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for PORT in range(100):
  client.connect((IP, PORT))
  response = client.recv(4096)
  print(response.decode())
  client.close()