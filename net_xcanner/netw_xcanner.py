#!usr/bin/env python3

import scapy.all as scapy

def xcann(ip):
    arp_req = scapy.ARP(pdst=ip)
    arp_req.show()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast.show()
    arp_req_broadcast = broadcast / arp_req
    arp_req_broadcast.show()

xcann("192.168.1.1/24")