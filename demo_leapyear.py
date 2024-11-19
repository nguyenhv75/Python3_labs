#! /usr/bin/env python3
# Author: Hien Nguyen
# Version: 1.0
# Description: This script will demo leap years test
"""
    Docstring:
"""
y = int(input('Please enter a year: '))

if y%4 == 0 and (y%400 == 0 or y%100 != 0):
    print("Leap Year")
else:
    print("NOT a leap year")
