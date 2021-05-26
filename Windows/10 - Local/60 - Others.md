# List logon requirements
Useful to check if brute forcing is possible.

```powershell
net accounts
````


# List drives
List all local drives:
```powershell
wmic logicaldisk get caption
# OR
wmic logicaldisk get caption,description,providername
```

```powershell
fsutil fsinfo drives
```

```powershell
Get-PSDrive | where {$_.Provider -like "Microsoft.PowerShell.Core\FileSystem"}| Format-Table Name,Root
```


# Default writeable folders
* `C:\Windows\System32\Microsoft\Crypto\RSA\MachineKeys`
* `C:\Windows\System32\spool\drivers\color`
* `C:\Windows\Tasks`
* `C:\windows\tracing`