# nmap

## Network scan
```bash
nmap -sn -n <SUBNET-RANGE>
```

List only IP's in network
```bash
nmap -sn -n <SUBNET-RANGE> | grep for | cut -d" " -f5
```
