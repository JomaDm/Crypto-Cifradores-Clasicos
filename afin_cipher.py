from file_manager import *


def gcd_euclides(a, b):
    if(b == 0):
        return 0
    
    while b != 0:
        q = a//b
        r = a - b * q
        a = b
        b = r
 
    return  a
    

def validate_key(a, n):
    if gcd_euclides(a, n) == 1:
        return True
    else:
        return False

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return -1
    else:
        return x % m

for i in range(26):
    print(f"from i: {i}  {validate_key(i, 26)} {modinv(i, 26)}"  )

