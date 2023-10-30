# Pentest


## Learn Python & Ethical Hacking 

---
* <a href="Tutorial.md">Tutorial.md</a>
---

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


## scripts

1. <a href="#port_scanner">Port Scanner</a>



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