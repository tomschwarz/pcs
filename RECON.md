# Recon
Tools and options I use for reconnaissance:
- [Nmap](#nmap)
- [NetCat](#netcat)
- [SMB](#smb)
- [DNS](#dns)
- [Web Enumeration](#web-enumeration)
- [Find SUID/SGID files](#find-suidsgid-files)

----

## Nmap

### Optional, but pleasant
Set ip address as a varible:  
```bash
export ip=10.10.10.123
``` 

Set network as a variable:  
```bash
export network=10.10.10.0/24
```

### Network scan
```bash
nmap -sn -n $network
```

List only IP's in network
```bash
nmap -sn -n $network | grep for | cut -d" " -f5
```

### Stealth scans
Normal stealth scan:  
```bash
nmap -sS $ip
```

Stealth FIN scan:  
```bash
nmap -sF $ip
```

### Service scans
Standard service/version scan:  
```bash
nmap -sV $ip
```

Service/version scan with script scan:  
```bash
nmap -sV -sC $ip
```

### System finger print
```bash
nmap -O $ip
```

### Quick scan
```bash
nmap -T4 -F $ip
```

### Evading firewals
```bash
nmap -P0 $ip
```

### Output scan into a file
```bash
nmap -sV -oN fileName $ip
```

----

## NetCat

### Port scan

Scan only one port:  
```bash
nc  -nvz $ip 80
```

Scan port range:  
```bash
nc -nvz $ip 0-1000
```

### Transferring files
From client to server:  
```bash
# Listener on server
nc -lvp 4444 > file-name.txt

## Sending from client
nc -v <IP> 4444 < file-name.txt
```

----

## SMB
Enumerate SMB shares:
```bash
smbmap -H <target>
# OR
smbclient -L <target>
```

Enumerate files and directories recursive on SMB shares:
```bash
smbmap -R --depth 5 -H <target>
```

Enumerate SMB with nmap:
```bash
# Enum shares
nmap --script smb-enum-shares -p 139,445 <target>

# Check for vulnerabilities
nmap --script smb-vuln* -p 139,445 <target>
```

Connect to a SMB share:
```bash
# Connect with no user (NULL session)
smbclient <target>
# OR
smbclient -U "" <target>
# OR
smbclient -U "" <target> -N
```

----

## DNS
Enumerate DNS with [dnsenum](https://github.com/fwaeytens/dnsenum):
```bash
# Avoiding reverse lookup (–noreverse)
dnsenum --noreverse -o dns-enum.xml <domain>
```

Enumerate DNS with nmap:
```bash
nmap -T4 -p 53 --script dns-brute <domain>
```

Enumerate DNS with [dnsrecon](https://github.com/darkoperator/dnsrecon):
```bash
dnsrecon -d <domain>
```

### Zone transfer
```bash
# Using "dig"
dig axfr @<ip> <domain>

# Using "host"
host -l <domain> <ip>
```

----

## Web Enumeration

## dirb
Standard dirb scan:  
```bash
dirb http://target.com /path/to/wordlist
```

Scan for extensions e.g. `.php`:  
```bash
dirb http://target.com /path/to/wordlist -X .php
```

## gobuster
Standard gobuster scan:  
```bash
gobuster dir -u https://target.com -w /usr/share/wordlists/dirb/big.txt
```

Scan for extensions e.g. `.php`:  
```bash
gobuster dir -u https://target.com -w /usr/share/wordlists/dirb/big.txt -x .php
```

Scan with blacklist on status codes e.g. `403,404`:  
```bash
gobuster dir -u https://target.com -w /usr/share/wordlists/dirb/big.txt -b 403,404
```

----

## Find SUID/SGID files
```bash
# Find files with SUID in current directory
find . -perm /4000

# Find files with SGID in current directory
find . -perm /2000

# Find files with SUID and SGID in current directory
find . -perm /6000
```