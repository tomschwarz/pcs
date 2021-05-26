# Firewall
## List firewall state and current configuration
```powershell
netsh advfirewall firewall dump
# OR
netsh firewall show state
netsh firewall show config
```

## List blocked ports
```powershell
$f=New-object -comObject HNetCfg.FwPolicy2;$f.rules |  where {$_.action -eq "0"} | select name,applicationname,localports
```

## Disable firewall
```powershell
netsh firewall set opmode disable
```

```powershell
netsh advfirewall set allprofiles state off
```


# Defender
## Status of defender
```powershell
Get-MpComputerStatus
```

## Disable real time monitoring
```powershell
Set-MpPreference -DisableRealtimeMonitoring $true; Get-MpComputerStatus
# AND
Set-MpPreference -DisableIOAVProtection $true
```

