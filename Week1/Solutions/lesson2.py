#! /usr/bin/python
'''
Prompt a user to enter in an IP address from standard input.
Read the IP address in and break it up into its octets.
Print out the octets in decimal, binary, and hex.

Your program output should look like the following:

 $ python exercise2.py

Please enter an IP address: 80.98.100.240

   Octet1         Octet2         Octet3         Octet4
-----------------------------------------------------------
     80             98             100            240
  0b1010000      0b1100010      0b1100100     0b11110000
    0x50           0x62           0x64           0xf0
-----------------------------------------------------------

Four columns, fifteen characters wide, a header column,
data centered in the column.
'''

from __future__ import print_function
'''
DOESN'T WORK
try:
    # PY2
    ip_address = raw_input("Please enter an IP address: ")
except NameError:
    # PY3
    ip_address = input("Please enter an IP address: ")
'''

ip_address = input("Please enter an IP address: ")

ip_address = ip_address.split(".")
header = ['Octet1', 'Octet2', 'Octet3', 'Octet4']

print("{:^15}{:^15}{:^15}{:^15}".format(*header))
print("-" * (15 * 4))
print("{:^15}{:^15}{:^15}{:^15}".format(*ip_address))
print("{:^15}{:^15}{:^15}{:^15}".format(
    bin(int(ip_address[0]))
    , bin(int(ip_address[1]))
    , bin(int(ip_address[2]))
    , bin(int(ip_address[3])))
)

print("{:^15}{:^15}{:^15}{:^15}".format(
    hex(int(ip_address[0]))
    , hex(int(ip_address[1]))
    , hex(int(ip_address[2]))
    , hex(int(ip_address[3])))
)
print("-" * (15 * 4))
