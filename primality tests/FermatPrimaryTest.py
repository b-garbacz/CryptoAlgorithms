def fermat(n, k) -> bool:
    if n % 2 == 0:
        return False
    for i in range(k):
        a = random.randint(2, n - 2)
        if fast_p(a, n - 1, n) != 1:
            return False
    return True