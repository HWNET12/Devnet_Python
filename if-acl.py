#!/usr/bin/python3

from re import A


aclNum = int(input("What is the IPv4 ACL number? "))
if aclNum >= 1 and aclNum <= 99:
    print("This is a standard IPv4 ACL.")
elif aclNum >= 1300 and aclNum <= 1999:
    print("This is a standard IPv4 ACL.")
elif aclNum >= 100 and aclNum <= 199:
    print("This is an extended IPv4 ACL")
elif aclNum >= 2000 and aclNum <= 2699:
    print("This is an extended IPv4 ACL")
else:
    print("This is not a standard or extended IPv4 ACL")