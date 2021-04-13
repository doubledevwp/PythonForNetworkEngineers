#!/usr/bin/env python
'''
Read the 'show_ipv6_intf.txt' file.

From this file, use Python regular expressions to extract the two IPv6 addresses.

The two relevant IPv6 addresses you need to extract are:

2001:11:2233::a1/24
2001:cc11:22bb:0:2ec2:60ff:fe4f:feb2/64
Try to use re.DOTALL flag as part of your search. Your search pattern should not
include any of the literal characters in the IPv6 address.

From this, create a list of IPv6 addresses that includes only the above two addresses.

Print this list to the screen.
'''

from __future__ import print_function
import re

with open('../assets/show_ipv6_intf.txt') as f:
    output = f.read()

# TODO: Not sure what to do here
found = re.search("IPv6 address:\s+(.*)\s+IPv6 subnet:", output, re.DOTALL)
ipv6_list = (found.group(1).strip()).splitlines()

for i, address in enumerate(ipv6_list[:]):
    address = re.sub("\[VALID\]", "", address)
    ipv6_list[i] = address.strip()

print(ipv6_list)
