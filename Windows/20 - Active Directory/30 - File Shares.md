**NOTE:** `powerview` is used to enumerate on `active directory` environments.
You have to disable `antivirus` for this. See here: [20 - Disable antivirus](20%20-%20Disable%20antivirus.md)

# Find shares in domain
```powershell
Find-DomainShare -Verbose
```

## Find non standard shares
```powershell
Find-DomainShare –Verbose -ExcludeStandard -ExcludeIPC -ExcludePrint
```


# Get file servers in domain
```powershell
Get-DomainFileServer -Verbose
```


# Find sensitive files in domain
```powershell
Invoke-FileFinder –Verbose
```