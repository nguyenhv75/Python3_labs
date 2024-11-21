#! /usr/bin/env python3
# Author: Hien Nguyen
# Version: 1.0
# Description: This script will demo different wasy of formatting strings
# using str concatenation and escape chars, str justification methods, the
# str format() method and f-strings (Py 3.5)!
"""
    Docstring:
"""
import sys
import re

if sys.platform == 'win32':
    file = r'c:\windows\system32\drivers\etc\services'
else:
    file = '/etc/services'

all_ports = set(range(1, 201))
used_ports = set()

with open(file, mode="rt") as fh_ports:
    for line in fh_ports:
        m = re.search(r"(\d+)/(tcp|udp)", line)
        if m:
            port = int(m.group(1))
            if port <= 200:
                used_ports.add(port)

print(f"All ports = {all_ports}")
print(f"Used ports = {used_ports}")
print(f"Unused ports = {all_ports - used_ports}")