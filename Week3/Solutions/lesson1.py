#!/usr/bin/env python
'''
Read the "show_vlan.txt" file into your program.
Loop through the lines in this file and extract all of the VLAN_ID, VLAN_NAME
combinations.
From these VLAN_ID and VLAN_NAME construct a new list where each element in
the list is a tuple consisting of (VLAN_ID, VLAN_NAME).
Print this data structure to the screen. Your output should look as follows:

[('1', 'default'),
('400', 'blue400'),
('401', 'blue401'),
('402', 'blue402'),
('403', 'blue403')]
'''

from __future__ import print_function
from pprint import pprint

with open("../assets/show_vlan.txt") as f:
    output = f.readlines()

new_list = []
for i in output:
    if i[0:4] in ["VLAN", "----"] or i.startswith(" "):
        continue
    new_list.append(tuple(i.split()[:2]))

pprint(new_list)
