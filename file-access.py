#!/usr/bin/python

from distutils.log import debug


devices = []
file = open("devices.txt", "r")
for item in file:
    item = item.strip()
    devices.append(item)
file.close()

print(type(devices))
