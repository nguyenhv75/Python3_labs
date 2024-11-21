#! /usr/bin/env python3
# Author: Hien Nguyen
# Version: 1.0
# Description: This script will demo different wasy of formatting strings
# using str concatenation and escape chars, str justification methods, the
# str format() method and f-strings (Py 3.5)!
"""
    Docstring:
"""
class Tank:
    def __init__(self, country, model):
        self.country = country
        self.model = model
        self._speed = 0
        self._direction = 0
        self._location = {'x':0, 'y':0, 'z':0}
        self._shells = 20
        self._health = 100

    def accel(self, increase):
        self._speed += increase

    def decel(selfself, decrease):
        self._spee
        self._speed -= decrease

    def rotate_left(self, degrees):
        self._direction -= degrees % 360
        return None

    def rotate_right(self, degrees):
        self._direction += degrees % 360
        return None

    def shoot(self):
        self._shells -= 1
        return None

    def take_damage(self, damage):
        self._health -= damage
        return None

    def __add__(self, other):
        return self._health + other._health