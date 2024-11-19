#! /usr/bin/env python3
# Author: Hien Nguyen
# Version: 1.0
# Description: This script will demo how to split and regoin stringss
# using the str .split() and .joint() methods.
"""
    Docstring:
"""

# Sample line from /etc/passwd on Linux for the root user account
# AND I want to modify the string! BUT str are IMMUTABLE!
line = "root:x:0:0:The Super User:/root/:/bin/ksh"

fields = line.split(":") # Return a MUTABLE list of objects.
fields[4] = "The Administrator"
fields[6] = ("/bin/bash")

line = ":".join(fields) #Return a NEW string separated with a colon.
print(line)