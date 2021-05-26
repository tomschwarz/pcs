# Find SUID/SGID files

## SUID
Find files with `SUID` in current directory:
```bash
find . -perm /4000
```

## SGID
Find files with `SGID` in current directory:
```bash
find . -perm /2000
```

## SUID & SGID
FInd files with `SUID` and `SGID` in current directory:
```bash
find . -perm /6000
```
