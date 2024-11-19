#! /usr/bin/env python3
# Author: Hien Nguyen
# Version: 1.0
# Description: This script will display a range of numbers by steps of -2.
"""
    Docstring:
"""
import sys

var = input("Please enter and integer:")
if not var.isdecimal():
    print("Invalid integer:", var)
    sys.exit(1)

for var in range(int(var), -1, -2):
    print(var)