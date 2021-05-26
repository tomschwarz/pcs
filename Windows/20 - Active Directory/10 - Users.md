**NOTE:** `powerview` is used to enumerate on `active directory` environments.
You have to disable `antivirus` for this. See here: [20 - Disable antivirus](20%20-%20Disable%20antivirus.md)

# List domain users
Get all domain users:
```powershell
Get-DomainUser
```

Get informations about an specific domain user:
```powershell
Get-DomainUser -Name <USERNAME>
```


# Find service accounts
```powershell
Get-DomainUser -SPN
```


# Get properties for domain users
```powershell
Get-DomainUser –Properties <PROPERTY-NAME>
```

Some interessting properties:
```powershell
Get-DomainUser –Properties pwdlastset
Get-DomainUser –Properties badpwdcount
Get-DomainUser –Properties lastlogon
Get-DomainUser -Properties samaccountname,description
```

## Check user description
Never forget to check the property `description`. Sometimes there are pretty useful informations, e.g. Passwords, Hashes and more!
```powershell
Get-DomainUser –Properties description
```


# Get enabled domain users
```powershell
Get-DomainUser -UACFilter NOT_ACCOUNTDISABLE -Properties distinguishedname
```


# Get disabled domain users
```powershell
Get-DomainUser -UACFilter ACCOUNTDISABLE
```