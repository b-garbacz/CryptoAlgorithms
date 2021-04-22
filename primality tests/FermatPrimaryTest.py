def fast_p(a, b, n) -> object:
    e = dec2bin(b)
    c = 1
    for i in range(0, len(e)):
        c = (c ** 2) % n
        if e[i] == 1:
            c = (c * a) % n
    return c

def fermat(n, k) -> bool:
    if n % 2 == 0:
        return False
    for i in range(k):
        a = random.randint(2, n - 2)
        if fast_p(a, n - 1, n) != 1:
            return False
    return True