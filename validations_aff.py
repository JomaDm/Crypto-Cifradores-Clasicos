def gcd_euclides(a, b):
    if(b == 0):
        return 0

    while b != 0:
        q = a//b
        r = a - b * q
        a = b
        b = r

    return a

# Valida llave *


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


if __name__ == '__main__':
    print("a=5 n=30 =", gcd_euclides(5, 30))
    print("a=97 n=239 =", gcd_euclides(97, 239))
    print("a=11111 n=12345 = ", gcd_euclides(11111, 12345))
    print("a=13 n=99991 =", gcd_euclides(13, 99991))
    print("a=10009 n=104729 =", gcd_euclides(10009, 104729))

    # for i in range(26):
    #     print(f"from i: {i}  {validate_key(i, 26)} {modinv(i, 26)}")
