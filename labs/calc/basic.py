import sys

def add(*args):
    """ Return SUM of all parameters as a float """
    total = 0
    for num in args:
        total += num
    return float(total)

def sub(x, z):
    """ Return result of x substract x as a float """
    return float(x-z)

def mul(*args):
    """ Return PRODUCT of all parameters as a float """
    total = 1
    for num in args:
        total *= num
    return float(total)

def div(x, z):
    """ Return Quotient of x divided by z to 3 decimal places """
    return round(x/z, 3)

(print("***** BASIC Calculator APP *****"))
print(f"4 + 3 = {add(4, 3)}")
print(f"4 + 3 +2 +1 = {add(4, 3, 2, 1)}")
print(f"4 * 3 = {mul(4, 3)}")
print(f"4 * 3 * 2 = {mul(4, 3, 2)}")
print(f"4 - 3 = {sub(4, 3)}")
print(f"4 / 3 ={div(4, 3)}")

sys.exit(0)