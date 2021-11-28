#!usr/bin/env python3

import subprocess

def decorator():
    print("--" * 35)

decorator()
print("Enter the interface:(eth0/enp1s0f0 || wlan0/wlp2s0)")
interface = input("interface :> ")

decorator()
print("Enter the MAC:(00:00:00:00:00:00)")
nw_mac_address= input("MAC :> ")

def macXanger(interface, nw_mac_address):

    decorator()
    print(" | + | Changing MAC address for " + interface + " to: " + nw_mac_address)
    decorator()
    
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", nw_mac_address])
    subprocess.call(["ifconfig", interface, "up"])
    subprocess.call(["ifconfig", interface])

macXanger(interface, nw_mac_address)