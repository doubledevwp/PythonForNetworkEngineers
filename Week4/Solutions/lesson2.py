#!/usr/bin/env python
'''
Create three separate lists of IP addresses.
The first list should be the IP addresses of the Houston data center routers,
and it should have over ten RFC1918 IP addresses in it
(including some duplicate IP addresses).

The second list should be the IP addresses of the Atlanta data center routers,
and it should have at least eight RFC1918 IP addresses
(including some addresses that overlap with the Houston data center).

The third list should be the IP addresses of the Chicago data center routers,
and it should have at least eight RFC1918 IP addresses.
The Chicago IP addresses should have some overlap with both the IP addresses
in Houston and Atlanta.

Convert each of these three lists to a set.

Using a set operation, find the IP addresses that are duplicated between Houston and Atlanta.

Using set operations, find the IP addresses that are duplicated in all three sites.

Using set operations, find the IP addresses that are entirely unique in Chicago.
'''

from __future__ import print_function

base_ip_houston = "10.10."
base_ip_atlanta = "172.1."
base_ip_chicago = "192.168."
houston_data_center = []
atlanta_data_center = []
chicago_data_center = []

for i in range(10):
    houston_data_center.append(base_ip_houston + str(i) + ".1")
    if(i == 5):
        houston_data_center.append(base_ip_houston + str(i) + ".1")
houston_data_center_set = set(houston_data_center)

for i in range(8):
    atlanta_data_center.append(base_ip_atlanta + str(i) + ".1")
    if(i == 2):
        atlanta_data_center.append(houston_data_center[i])
atlanta_data_center_set = set(atlanta_data_center)

for i in range(8):
    chicago_data_center.append(base_ip_chicago + str(i) + ".1")
    if(i == 2):
        chicago_data_center.append(houston_data_center[i])
        chicago_data_center.append(atlanta_data_center[i])
chicago_data_center_set = set(chicago_data_center)

print("Duplicate IP Address for Houston & Atlanta are:", houston_data_center_set.intersection(
    atlanta_data_center_set))
print('-' * 80)

print(
    "Duplicate IP Address for Houston, Atlanta & Chicago are:",
    houston_data_center_set.intersection(
        atlanta_data_center_set.intersection(chicago_data_center_set)))
print('-' * 80)

print("Unique IP Addresses for Chicago are:", chicago_data_center_set.difference(
    atlanta_data_center_set).difference(
        houston_data_center))
