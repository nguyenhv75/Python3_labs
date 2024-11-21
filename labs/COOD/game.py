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
import tank

def main():
    thomas_tank = tank.Tank("german", "tiger")
    rick_tank = tank.Tank("american", "sherman")
    rajat_tank = tank.Tank("british", "churchill")

    thomas_tank.accel(39)
    rick_tank.accel(28)

    rajat_tank.rotate_left(289)
    rajat_tank.accel(31)
    rajat_tank.shoot()

    thomas_tank.take_damage(62)
    rick_tank.take_damage(22)

    print(f"Thomas's tank has health of {thomas_tank._health}")

    print(f"Status of Thomas's and Rick's Tank = {thomas_tank + rick_tank}")

    return None

if __name__ == "__main__":
    main()
    sys.exit(0)