#! /usr/bin/python
'''
Create a show_version variable that contains the following

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "

Remove all leading and trailing whitespace from the string.
Split the string and extract the model and serial_number from it.
Check if 'Cisco' is contained in the model string (ignore capitalization).
Check if '881' is in the model string.
Print out both the serial number and the model.
'''

from __future__ import print_function

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "

extra_number, model_number, serial_number = show_version.strip().split()

print("Is this a CISCO device? {}".format("cisco" in model_number.lower()))
print("Is this model number 881? {}".format("881" in model_number))
print("Model number: {}".format(model_number))
print("Serial number: {}".format(serial_number))
