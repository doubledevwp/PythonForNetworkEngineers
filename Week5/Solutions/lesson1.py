#!/usr/bin/env python
'''
Create an ssh_conn function.
This function should have three parameters: ip_addr, username, and password.
The function should print out each of these three variables and clearly indicate
which variable it is printing out.

Call this ssh_conn function using entirely positional arguments.

Call this ssh_conn function using entirely named arguments.

Call this ssh_conn function using a mix of positional and named arguments.
'''

from __future__ import print_function

def ssh_conn(ip_addr, username, password):
    print("IP Address: ", ip_addr)
    print("Username: ", username)
    print("Password: ", password)
    print('-------------' * 2)

ssh_conn('192.1.0.123', 'testerson', 'urmom')
ssh_conn(username='what is this?', ip_addr='123.12.32.41', password='eatmyshorts')
ssh_conn('23.41.323.44', password='password123', username='Jack')
