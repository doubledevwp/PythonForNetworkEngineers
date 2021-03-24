#!/usr/bin/env python
'''
Construct a list of 254 IP addresses. The base IP address should be equal to
'192.168.1.0' or '192.168.1.'.

You should use the 'range' builtin to accomplish this.

Your list should have all of the IP addresses from 192.168.1.1 to 192.168.1.254.

Use Python's 'enumerate' to print out all of the IP addresses and their corresponding
list index. The output should look similar to the following:

0 ---> 192.168.1.1
1 ---> 192.168.1.2
2 ---> 192.168.1.3
3 ---> 192.168.1.4
4 ---> 192.168.1.5
...

Use a list slice to create a new list that goes from 192.168.1.3 to 192.168.1.6.

Using a loop and os.system("ping -c 3 192.168.1.3") try pinging all of the IP addresses
in this short list.

For Windows the command will probably be os.system("ping -n 3 192.168.1.3").

Put a variable at the top to define whether you are using Windows or Linux/MacOs.
This should be similar to the following:

WINDOWS = False

base_cmd_linux = 'ping -c 2'
base_cmd_windows = 'ping -n 2'
# Ternary operator
base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux
'''

from __future__ import print_function
import os  # for os.system ping
import sys  # sys.platform detect OS

ip_addresses = []
base_ip = '192.168.1.'
WINDOWS = True if sys.platform == 'win32' else False
base_cmd_linux = 'ping -c 2 '
base_cmd_windows = 'ping -n 2 '
cmd = base_cmd_windows if WINDOWS else base_cmd_linux

for i in range(255):
    ip_addresses.append(base_ip + str(i))

for i, ip_address in enumerate(ip_addresses):
    print("{} ---> {}".format(i, ip_address))

ip_addresses_slice = ip_addresses[100:107]

for i in ip_addresses_slice:
    print("\n--> Pinging IP Address: {}".format(i))
    os.system("{} {}".format(cmd, i))
