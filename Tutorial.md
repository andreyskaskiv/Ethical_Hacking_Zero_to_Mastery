 ```bash
 pip install --upgrade pip
 pip install -r requirements.txt
 ```
~~~shell
$ pip freeze > requirements.txt
~~~


1. <a href="#port_scanner">Port Scanner</a>



---

### 1. **Port Scanner** <a name="port_scanner"></a> 

    ```pycon
    cd 1_port_scan
    ```
    ```pycon
    ┌──(kali㉿kali)-[~/PycharmProjects/Complete_EH_Bootcamp_Zero_to_Mastery/1_port_scan]
    └─$ python3 port_scanner_1.py -t 10.0.2.4 -p 100
    
    Starting Start For 10.0.2.4:
    [+] Port Opened 21
    [+] Port Opened 22
    [+] Port Opened 23
    [+] Port Opened 25
    [+] Port Opened 53
    [+] Port Opened 80
    ```
    
    Some servers may consider such requests as a hacking attempt and block your IP address:
    ```pycon
    ┌──(kali㉿kali)-[~/PycharmProjects/Complete_EH_Bootcamp_Zero_to_Mastery/1_port_scan]
    └─$ python3 port_scanner_2.py -t 10.0.2.1,10.0.2.4 -p 100
    [*] Scanning Multiple Targets
    
    Starting Start For 10.0.2.1:
    
    Starting Start For 10.0.2.4:
    [+] Port Opened 21
    Banner: b'220 (vsFTPd 2.3.4)\r\n530 Please login with USER and PASS.\r\n'
    
    [+] Port Opened 22
    Banner: b'SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1\n'
    
    [+] Port Opened 23
    Banner: b"\xff\xfd\x18\xff\xfd \xff\xfd#\xff\xfd'"
    
    [+] Port Opened 25
    Banner: b'220 metasploitable.localdomain ESMTP Postfix (Ubuntu)\r\n'
    
    [+] Port Opened 53
    Banner: b''
    
    [+] Port Opened 80
    Banner: b'<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">\n<html><head>\n<title>400 Bad Request</title>\n</head><body>\n<h1>Bad Request</h1>\n<p>Your browser sent a request that this server could not understand.<br />\n</p>\n<hr>\n<address>Apache/2.2.8 (Ubuntu) DAV/2 Server at metasploitable.localdomain Port 80</address>\n</body></html>\n'
    
    ```


