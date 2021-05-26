# Web-Enumeration

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
