# Windows Port Forwarding

## Powershell
```powershell
netsh interface portproxy add v4tov4 listenaddress=<localaddress> listenport=<localport> connectaddress=<destaddress> connectport=<destport>
```

## Command line
```powershell
plink.exe <user>@<kali> -R <kali-port>:<target-IP>:<target-port>
```