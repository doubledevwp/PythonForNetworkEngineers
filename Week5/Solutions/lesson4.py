#!/usr/bin/env python
'''
Similar to lesson3, exercise4 write a function that normalizes a MAC
address to the following format:

01:23:45:67:89:AB

This function should handle the lower-case to upper-case conversion.
It should also handle converting from '0000.aaaa.bbbb' and from
'00-00-aa-aa-bb-bb' formats.

The function should have one parameter, the mac_address. It should return
the normalized MAC address
Single digit bytes should be zero-padded to two digits. In other words, this:

a:b:c:d:e:f

should be converted to:

0A:0B:0C:0D:0E:0F

Write several test cases for your function and verify it is working properly.
'''

from __future__ import print_function
import re


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


print("Normalized MAC Address: ", normalize_mac_address('123.234.456'))
print("Normalized MAC Address: ", normalize_mac_address('aabb.ccdd.eeff'))
print("Normalized MAC Address: ", normalize_mac_address('a:b:c:d:e:f'))
print("Normalized MAC Address: ", normalize_mac_address('0000.aaaa.bbbb'))
print("Normalized MAC Address: ", normalize_mac_address('123.456.789'))
print("Normalized MAC Address: ", normalize_mac_address('a-b-c-d-e-f'))
print("Normalized MAC Address: ", normalize_mac_address('1-2-a-b-3-44'))
