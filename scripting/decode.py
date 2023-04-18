#!/usr/bin/python3

import base64

#Open File
with open('b64.txt') as f:
	msg = f.read()

#Decode 50 times
for i in range(50):
	msg = base64.b64decode(msg)

print(f"The flag is: {msg.decode('utf8')}")