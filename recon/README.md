# Recon
Tools and options I use for reconnaissance:
- [Nmap](#nmap)
- [NetCat](#)
- [Web Enumeration](#)

----

## Nmap

### Optional, but pleasant
Set ip address as a varible:  
```bash
export ip=10.10.10.123
``` 

Set network as a variable:  
```bash
export netw=10.10.10.0/24
```

### Network scan
```bash
nmap -sn -n $netw | grep for | cut -d" " -f5
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

### Output scan into a file
```bash
nmap -sV -oN fileName $ip
```
