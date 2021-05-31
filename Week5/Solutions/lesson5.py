#!/usr/bin/env python
'''
Copy your solution from exercise3 to exercise4. Add an 'import pdb' and pdb.set_trace()
statement outside of your function (i.e. where you have your function calls).

Inside of pdb, experiment with:

Listing your code.
Using 'next' and 'step' to walk through your code. Make sure you understand the difference
between next and step.
Experiment with 'up' and 'down' to move up and down the code stack.
Use p to inspect a variable.
Set a breakpoint and run your code to the breakpoint.
Use '!command' to change a variable (for example !new_mac = []) 
'''

from __future__ import print_function
import re
import pdb


def normalize_mac_address(mac_address):
    mac_address = mac_address.upper()  # .split('.')
    new_mac = []

    if ":" in mac_address or "-" in mac_address:  # len(mac_address[k]) == 4:
        octets = re.split(r"[-:]", mac_address)

        for octet in octets:
            if len(octet) < 2:
                octet = octet.zfill(2)
            new_mac.append(octet)

    elif "." in mac_address:
        octets = mac_address.split(".")

        if len(octets) != 3:
            raise ValueError("Something went wrong!")
        
        for octet in octets:
            if len(octet) < 4:
                octet = octet.zfill(4)
            
            new_mac.append(octet[:2])
            new_mac.append(octet[2:])

    print(" Incoming MAC Address: ", mac_address)
    print("Formatted MAC Address: ", new_mac)

    # new_mac = new_mac[:-1]
    return ":".join(new_mac)

pdb.set_trace()
print("Normalized MAC Address: ", normalize_mac_address('123.234.456'))
print("Normalized MAC Address: ", normalize_mac_address('aabb.ccdd.eeff'))
print("Normalized MAC Address: ", normalize_mac_address('a:b:c:d:e:f'))
print("Normalized MAC Address: ", normalize_mac_address('0000.aaaa.bbbb'))
print("Normalized MAC Address: ", normalize_mac_address('123.456.789'))
print("Normalized MAC Address: ", normalize_mac_address('a-b-c-d-e-f'))
print("Normalized MAC Address: ", normalize_mac_address('1-2-a-b-3-44'))
