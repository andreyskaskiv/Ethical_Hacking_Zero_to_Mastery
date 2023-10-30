#! /usr/bin/python
"""Primitive port scanner"""
import socket

import termcolor

from configurations.reading_argparse import get_argparse


def get_banner(sock):
    """We get the banner of this port"""
    try:
        sock.send(b'GET HTTP/1.1 \r\n')
        banner = sock.recv(1024)
        print(f"Banner: {banner}\n")
        sock.close()
    except:
        pass


def scan_port(ip_address, port):
    """We check whether a certain port is open on a certain IP address."""
    try:
        sock = socket.socket()
        sock.connect((ip_address, port))
        print(f"[+] Port Opened {port}")
        return sock
    except:
        return None


def scan(target: str, ports: int):
    """Scan multiple ports on a specific IP address"""
    print(termcolor.colored(f"\nStarting Start For {target}:", "magenta"))
    for port in range(1, ports):
        sock = scan_port(target, port)

        if sock is not None:
            get_banner(sock)


def main(targets: str, ports: int):
    """Main controller"""
    if "," in targets:
        print(termcolor.colored("[*] Scanning Multiple Targets", "green"))
        for ip_addr in targets.split(","):
            scan(ip_addr.strip(' '), ports)

    else:
        scan(targets, ports)


if __name__ == '__main__':
    ip_of_target_machines, number_of_ports = get_argparse()
    main(ip_of_target_machines, number_of_ports)
