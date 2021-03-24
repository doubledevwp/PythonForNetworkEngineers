#!/usr/bin/env python
'''
Read the contents of the "show_arp.txt" file.
Using a for loop, iterate over the lines of this file.
Process the lines of the file and separate out the ip_addr and mac_addr
for each entry into a separate variable.

Add a conditional statement that searches for '10.220.88.1'.
If 10.220.88.1 is found, print out the string "Default gateway IP/Mac"
and the corresponding IP address and MAC Address.

Using a conditional statement, also search for '10.220.88.30'.
If this IP address is found, then print out "Arista3 IP/Mac is" and
the corresponding ip_addr and mac_addr.

Keep track of whether you have found both the Default Gateway and the
Arista3 switch. Once you have found both of these devices, break out of the for loop.
'''

from __future__ import print_function

with open("../assets/show_arp.txt") as f:
    output = f.readlines()

default_gateway_flag = arista_flag = False
for i in output:
    ip_address = i.split()[1]
    mac_address = i.split()[3]

    if "10.220.88.1" in ip_address:
        print("Default gateway IP/Mac: {}/{}".format(ip_address, mac_address))
        default_gateway_flag = True
    elif "10.220.88.30" in ip_address:
        print("Arista3 IP/Mac is: {}/{}".format(ip_address, mac_address))
        arista_flag = True

    if default_gateway_flag and arista_flag:
        break
