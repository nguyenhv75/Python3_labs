#! /usr/bin/env python3
# Author: Hien Nguyen
# Version: 1.0
# Description: This script will display the files in your home directory
# with their size
"""
    Docstring:
"""
import sys
import glob
import os

# Get the directory name.
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern.
pattern = os.path.join(hdir, '*')

# Use the glob.glob() function to obtain the list of filenames.
for filename in glob.glob(pattern):

    # Use os.path.getsize to find each file's size.
    size = os.path.getsize(filename)

    # Only display files that are not zero length.
    if size > 0:
        print(os.path.basename(filename), size, 'bytes')
