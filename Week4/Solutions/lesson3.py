#!/usr/bin/env python
'''
Read in the 'show_version.txt' file.
From this file, use regular expressions to extract the OS version, serial number,
and configuration register values.

Your output should look as follows:

OS Version: 15.4(2)
T1 Serial Number: FTX0000038X
​Config Register: 0x2102
'''

from __future__ import print_function
import re

with open('./assets/show_version.txt') as f:
    output = f.read()

found = re.search("^Cisco .* Version (.*),", output, re.M)
if found:
    os_version = found.group(1)

found = re.search("^Processor .* (.*)$", output, re.M)
if found:
    serial_number = found.group(1)

found = re.search("^Configuration.* (\S+)$", output, re.M)
if found:
    config_reg = found.group(1)

print("OS Version:", os_version)
print("T1 Serial Number:", serial_number)
print("Configuration Register:", config_reg)
