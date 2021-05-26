# List all local groups
```powershell
net localgroup
```

```powershell
Get-LocalGroup | Format-Table Name
```


# Get Details about a group
```powershell
net localgroup <GROUPNAME>
```

```powershell
Get-LocalGroupMember <GROUPNAME> | Format-Table Name,PrincipalSource
```
