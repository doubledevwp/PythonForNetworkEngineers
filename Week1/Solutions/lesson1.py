#! /usr/bin/python
'''
Create a Python script that has three variables: ip_addr1, ip_addr2, ip_addr3
(representing three corresponding IP addresses).
Print these three variables to standard output using a single print statement.

Make your print statement compatible with both Python2 and Python3.

If you are using either Linux or MacOS make your program executable by adding
a shebang line and by changing the files permissions
(i.e. chmod 755 exercise1.py
'''

from __future__ import print_function

ip_address1 = '192.168.1.1'
ip_address2 = '192.168.1.2'
ip_address3 = '192.168.1.3'

print(ip_address1, ip_address2, ip_address3)
