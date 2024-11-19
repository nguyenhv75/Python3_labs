#! /usr/bin/env python3
# Author: Hien Nguyen
# Version: 1.0
# Description: This script will simulate a bank PIN machine using GETPASS module
# Max 3 attempts!
"""
Docstring:
"""
import sys
import getpass

master_pin = "0123"
pin = None
tries = 0

while pin != master_pin and tries < 3:
    pin = getpass.getpass("Enter PIN: ")
    if pin == master_pin:
        print("Valid PIN")
        break
    else:
        print("Invalid PIN")
        tries += 1
else:
    # Executes only ONCE when condition becomes False!
    print("You had", tries, "tries and failed!")
    print("Your card has been retained. Have a nice day :-)")

print("Done.")