#! /usr/bin/python
'''
Create three different variables the first variable should use all lower case
characters with underscore ( _ ) as the word separator.
The second variable should use all upper case characters with underscore as
the word separator. The third variable should use numbers, letters, and underscore,
but still be a valid variable Python variable name.

Make all three variables be strings that refer to IPv6 addresses.

Use the from future technique so that any string literals in Python2 are unicode.

compare if variable1 equals variable2
compare if variable1 is not equal to variable3
'''

from __future__ import unicode_literals

ip_address = '192.168.1.1'
IP_ADDRESS = '192.168.1.2'
IP_Address3 = '192.168.1.3'

print("Are {} and {} the same? {}".format(ip_address, IP_ADDRESS, (ip_address == IP_ADDRESS)))
print("Are {} and {} NOT the same? {}".format(ip_address, IP_Address3, (ip_address != IP_Address3)))
