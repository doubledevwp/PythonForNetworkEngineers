#!/usr/bin/env python
'''
Expand on the ssh_conn function from exercise1 except add a fourth parameter
'device_type' with a default value of 'cisco_ios'.
Print all four of the function variables out as part of the function's execution.

Call the 'ssh_conn2' function both with and without specifying the device_type

Create a dictionary that maps to the function's parameters.
Call this ssh_conn2 function using the **kwargs technique.
'''

from __future__ import print_function

def ssh_conn2(ip_addr, username, password, device_type='cisco_ios'):
    print("IP Address: ", ip_addr)
    print("Username: ", username)
    print("Password: ", password)
    print("Device Type: ", device_type)
    print('-------------' * 2)

ssh_conn2('192.1.0.123', 'testerson', 'urmom')
ssh_conn2('123.123.123.123', device_type='tenda wifi', password='qwerty123easy', username='yessireebob')

func_params = {'ip_addr': '12.23.34.45',
               'username': 'godmode',
               'password': 'zues'}

ssh_conn2(**func_params)
