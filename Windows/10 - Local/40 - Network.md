# Network inferfaces
How to list all network interfaces, IP and DNS.
```powershell
ipconfig /all
```

```powershell
Get-NetIPConfiguration | Format-Table InterfaceAlias,InterfaceDescription,IPv4Address
```

```powershell
Get-DnsClientServerAddress -AddressFamily IPv4 | Format-Table
```


# List current routing table
```powershell
route print
```

```powershell
Get-NetRoute -AddressFamily IPv4 | Format-Table DestinationPrefix,NextHop,RouteMetric,ifIndex
```


# List ARP table
```powershell
arp -A
```

```powershell
Get-NetNeighbor -AddressFamily IPv4 | Format-Table ifIndex,IPAddress,LinkLayerAddress,State
```


# List current connections
```powershell
netstat -ano
```


# List network shares
```powershell
net share
```


# SNMP Configuration
```powershell
reg query HKLM\SYSTEM\CurrentControlSet\Services\SNMP /s
# OR
Get-ChildItem -path HKLM:\SYSTEM\CurrentControlSet\Services\SNMP -Recurse
```