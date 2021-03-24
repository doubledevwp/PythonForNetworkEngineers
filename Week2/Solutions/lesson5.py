#!/usr/bin/env python
'''
Read the 'show_ip_bgp_summ.txt' file into your program.
From this BGP output obtain the first and last lines of the output.

From the first line use the string .split() method to obtain the
local AS number.

From the last line use the string .split() method to obtain the
BGP peer IP address.

Print both local AS number and the BGP peer IP address to the screen.
'''

from __future__ import print_function

with open("../assets/show_ip_bgp_summ.txt") as f:
    output = f.readlines()

first_line = output[0].split()[-1]
print("Local As Number:", first_line)

last_line = output[-1].split()[0]
print("BGP Peer IP Address:", last_line)
