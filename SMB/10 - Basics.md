# SMB

Enumerate SMB shares:
```bash
smbmap -H <TARGET>
# OR
smbclient -L <TARGET>
```

Enumerate files and directories recursive on SMB shares:
```bash
smbmap -R --depth 5 -H <TARGET>
```

Enumerate SMB with nmap:
```bash
# Enum shares
nmap --script smb-enum-shares -p 139,445 <TARGET>

# Check for vulnerabilities
nmap --script smb-vuln* -p 139,445 <TARGET>
```

Connect to a SMB share:
```bash
# Connect with no user (NULL session)
smbclient \\\\<IP>\\<SHARE>
# OR
smbclient -U "" \\\\<IP>\\<SHARE>
# OR
smbclient -U "" \\\\<IP>\\<SHARE> -N
```
