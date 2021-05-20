#!/usr/bin/env python
'''
Create a function that randomly generates an IP address for a network.
The default base network should be '10.10.10.'. For simplicity the network will always be a /24.

You should be able to pass a different base network into your function as an argument.

Randomly pick a number between 1 and 254 for the last octet and return the full IP address.

You can use the following to randomly generate the last octet:

import random
random.randint(1, 254)

Call your function using no arguments.
Call your function using a positional argument.
Call your function using a named argument.

For each function call print the returned IP address to the screen.
'''

from __future__ import print_function
import random


def random_ip_address_generator(base='10.10.10.'):
    last_octet = str(random.randint(1, 254))
    ip_address = base + last_octet
    return ip_address


print(random_ip_address_generator())
print(random_ip_address_generator('172.1.2.'))
print(random_ip_address_generator(base='192.168.1.'))
