#!usr/bin/env python3

import scapy.all as scapy

def decor():
    print("****" * 15)

    # To decorate the output program to make more readble

def xcann(ip):
    arp_req = scapy.ARP(pdst=ip) # here we are making the request by the arp
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # here we are puting the interface of output
    arp_req_broadcast = broadcast / arp_req # here we are getting all information from the request 
    answered_list = scapy.srp(arp_req_broadcast, timeout= 1, verbose= False)[0]

    # The send n receive funtions family is the heart of scapy
    # They return a couple of two lists. The first element is a
    # list of couples(packet sent, answer), and the second element
    # is the list of unanswered packets. 

    print("\n" + "IP \t\t\t MAC ADDRESS")
    print("----" *15)

    for answer in answered_list:
        print(answer[1].psrc + " \t\t " + answer[1].hwsrc)

    decor()

xcann("192.168.1.1/24")