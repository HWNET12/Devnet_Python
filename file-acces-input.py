#!/usr/bin/python3

from hashlib import new


file = open('devices.txt', 'a')
while True:
    newItem = input("Enter the new device: ")
    if newItem == "exit":
        print("All done!")
        break
    file.write(newItem + "\n")
file.close()