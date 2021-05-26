# nc = NetCat

## Transferring files
From client to server:  
```bash
# Listener on server
nc -lvp 4444 > <FILE>

## Sending from client
nc -v <IP> 4444 < <FILE>
```