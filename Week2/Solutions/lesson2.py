#! /usr/bin/python
'''
Create a list of five IP addresses.

Use the .append() method to add an IP address onto the end of the list.
Use the .extend() method to add two more IP addresses to the end of the list.

Use list concatenation to add two more IP addresses to the end of the list.

Print out the entire list of ip addresses.
Print out the first IP address in the list.
Print out the last IP address in the list.

Using the .pop() method to remove the first IP address in the list
and the last IP address in the list.

Update the new first IP address in the list to be '2.2.2.2'.
Print out the new first IP address in the list.
'''

from __future__ import print_function

ip_address_list = ['192.168.1.0', '192.168.1.', '192.168.1.2', '192.168.1.3', '192.168.1.4']
ip_address_list.append('10.10.0.1')
ip_address_list.extend(['17.22.1.0', '17.22.1.1'])
ip_address_list += ['22.2.2.2', '22.2.2.3']

print("The list of IP Addresses:", ip_address_list)
print("The first IP Address is:", ip_address_list[0])
print("The last IP Address is:", ip_address_list[-1])

ip_address_list.pop(0)
ip_address_list.pop()

ip_address_list[0] = '2.2.2.2'
print("The new first IP Address is:", ip_address_list[0])
