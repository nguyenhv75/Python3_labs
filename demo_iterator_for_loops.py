#! /usr/bin/env python3
# Author: Hien Nguyen
# Version: 1.0
# Description: This script will demo how to ITERATE through a COLLEXTION
# (str/tuples/list/dict/sets) using an ITERATOR for loop.
"""
    Docstring:
"""
films = ['casablanca', 'enter the dragon', 'fist of fury', 'waterloo', 'gladiator']

# Iterate through a COLLECTION using n ITERATOR for loop.
for film in films:
    print(film.title(), end="\n")
print("Films = ", films)

# Iterate through a COLLECTION AND modiy each value using
# an ITERATOR for loop and a counter.
idx=0
for film in films:
    print(film.upper(), end="\n")
    films[idx] = film.upper()
    idx += 1
print("Films = ", films)

# Alternatively we could Iterate through a COLLECTION and modiy
# the values using an ITERATOR for loop plus enumerate() function.
for (idx, film) in enumerate(films, start=0):
    print(film.lower(), end="\n")
    films[idx] = film.lower()
    idx += 1
print("Films = ", films)
