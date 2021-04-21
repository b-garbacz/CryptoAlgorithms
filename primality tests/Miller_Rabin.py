import random
from Tabofprimes import TabOfPrimes
import time

# FIXME: Miller-Rabin is not working for large prime numbers

def dec2bin(x):
    y = bin(x)[2:]
    tab = []
    for i in range(0, len(y)):
        tab.append(int(y[i]))
    return tab


def fast_p(a, b, n) -> object:
    e = dec2bin(b)
    c = 1
    for i in range(0, len(e)):
        c = (c ** 2) % n
        if e[i] == 1:
            c = (c * a) % n
    return c


def miller_rabin_test(n, k) -> bool:
    # obviously non prime
    if n <= 1:
        return False
    # composite
    if n % 2 == 0:
        return False
    s = 0
    d = n - 1
    while d % 2 == 0:
        s, d = s + 1, int(d / 2)
    for xd in range(k):
        a = random.randint(1, n - 1)
        x = fast_p(a, d, n)
        if x != 1:
            for r in range(0, s):
                if x != n - 1:
                    x = fast_p(x, 2, n)
                else:
                    break
            else:
                return False
    return True


def test():
    i = 0
    for x in range(0, len(TabOfPrimes)):  # len(Tab)=2657
        pt = miller_rabin_test(TabOfPrimes[x], 16)
        if pt is False:
            print("Not true that the number below is a composite number")
            print(TabOfPrimes[i])
        if pt is True:
            i += 1
    return i


print("Out of", len(TabOfPrimes), " test cases of prime numbers,", test(), "are positive for Miller-Rabin-Test")

start = time.time()
# but 3333 is composite = 3*11*101
print(miller_rabin_test(2222, 10))
print(time.time() - start)
