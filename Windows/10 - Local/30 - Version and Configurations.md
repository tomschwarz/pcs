# System informations
Get all system informations:
```powershell
systeminfo
```

Get system name and version:
```powershell
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
```


# Installed patches and updates
List installed patches and updates:
```powershell
wmic gfe
```


# System architecture
Get system architecture like 32-bit or 64-bit:
```powershell
wmic os get osarchitecture
```

```powershell
echo %PROCESSOR_ARCHITECTURE%
```


# Environment settings/variables
List the environment variables:
```powershell
Get-ChildItem Env: | Format-Table <KEY>,<VALUE>
```
