# DNS

Enumerate DNS with [dnsenum](https://github.com/fwaeytens/dnsenum):
```bash
# Avoiding reverse lookup (–noreverse)
dnsenum --noreverse -o dns-enum.xml <DOMAIN>
```

Enumerate DNS with nmap:
```bash
nmap -T4 -p 53 --script dns-brute <DOMAIN>
```

Enumerate DNS with [dnsrecon](https://github.com/darkoperator/dnsrecon):
```bash
dnsrecon -d <DOMAIN>
```
