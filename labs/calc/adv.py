import sys

def power(x, z):
    """  """
    return float(x**z)

def mod(x, z):
    """  """
    return float(x%z)

def sqrt(x):
    """  """
    return round(x**0.5, 3)

print("£££££")
print(f"5 ** 2 = {power(5, 2)}")
print(f"5 % 2 = {mod(5, 2)}")
print(f"Square Foot of 5 = {sqrt(5)}")

sys.exit(0)