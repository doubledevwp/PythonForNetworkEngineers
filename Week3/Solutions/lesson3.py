#!/usr/bin/env python
'''
Read the 'show_lldp_neighbors_detail.txt' file. Loop over the lines of this file.
Keep reading the lines until you have encountered the remote "System Name" and remote "Port id".
Save these two items into variables and print them to the screen. You should extract only the
system name and port id from the lines
(i.e. your variables should only have 'twb-sf-hpsw1' and '15').
Break out of your loop once you have retrieved these two items.
'''

from __future__ import print_function

with open("../assets/show_lldp_neighbors_detail.txt") as f:
    output = f.readlines()

system = port = None
for i in output:
    if "System Name:" in i:
        system = i.split(": ")[1]
    elif "Port id:" in i:
        port = i.split(": ")[1]

    if system and port:
        print("System Name: {}".format(system))
        print("Port Id: {}".format(port))
        break
