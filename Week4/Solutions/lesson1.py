#!/usr/bin/env python
'''
Create a dictionary representing a network device.
The dictionary should have key-value pairs representing the
'ip_addr', 'vendor', 'username', and 'password' fields.

Print out the 'ip_addr' key from the dictionary.

If the 'vendor' key is 'cisco', then set the 'platform' to 'ios'.
If the 'vendor' key is 'juniper', then set the 'platform' to 'junos'.

Create a second dictionary named 'bgp_fields'.
The 'bgp_fields' dictionary should have a keys for 'bgp_as',
'peer_as', and 'peer_ip'.

Using the .update() method add all of the 'bgp_fields' dictionary key-value
pairs to the network device dictionary.

Using a for-loop, iterate over the dictionary and print out all of the
dictionary keys.

Using a single for-loop, iterate over the dictionary and print out all
of the dictionary keys and values.
'''

from __future__ import print_function

network_devices = {
    'ip_address': '10.10.1.0',
    'vendor': 'Cisco',
    'username': 'user123',
    'password': 'abc'}

print("IP Address: ", network_devices['ip_address'])

network_devices['platform'] = 'ios' if network_devices['vendor'].lower() == 'cisco' else 'junos'

bgp_fields = {
    'bgp_as': '123',
    'peer_as': '456',
    'peer_ip': '198.168.1.1'}

network_devices.update(bgp_fields)

for k in network_devices:
    print("Key:", k)

print("-" * 10)
for k, v in network_devices.items():
    print("Key: ", k)
    print("Value: ", v)
    print("-" * 10)
