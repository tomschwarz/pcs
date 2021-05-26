# Current username
```powershell
echo %USERNAME%
```

```powershell
whoami
```

```powershell
$env:username
```


# List user privileges
```powershell
whoami /priv
```

```powershell
whoami /groups
```


# List all users
```powershell
net user
```

```powershell
whoami /all
```

```powershell
Get-LocalUser | Format-Table Name,Enaled,LastLogon
```

```powershell
Get-ChildItem C:\Users -Force | select Name
```


# Get details about a user
```powershell
net user <USERNAME>
```
