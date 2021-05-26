**NOTE:** `powerview` is used to enumerate on `active directory` environments.
You have to disable `antivirus` for this. See here: [20 - Disable antivirus](20%20-%20Disable%20antivirus.md)

# List domain groups
```powershell
Get-DomainGroup
```

Get members of specific domain group:
```powershell
Get-DomainGroupMember -Name "<GROUPNAME>"
```

Get groups of specific domain:
```powershell
Get-DomainGroup –Domain <DOMAIN-NAME>
```


# Get all members of domain group
```powershell
Get-NetGroupMember -GroupName <GROUP-NAME>
Get-NetGroupMember -GroupName <GROUP-NAME> -Recurse
Get-NetGroupMember -GroupName <GROUP-NAME> -Domain <DOMAIN-NAME>
```


# Get group membership of user
```powershell
Get-DomainGroup -UserName "<USERNAME>"
```
