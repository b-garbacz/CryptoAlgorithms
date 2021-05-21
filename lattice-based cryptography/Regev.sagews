def drg(x, sig, c):  # density function
    p = pow(e, - (pow(x - c, 2)) / (2 * pow(sig, 2)))
    return p


def sdrg(sig, c):  # sum of sersier
    sum = 0
    for x in range(-6 * sig, 6 * sig):
        sum += drg(x, sig, c)
    return sum


def probability(x, sig, c):  # probability
    return drg(x, sig, c) / sdrg(sig, c)


def generator(sig, c):
    sum = 0
    for x in range(-3 * sig, 1):
        sum += probability(x, sig, c)
    U = RR.random_element(sum, 1)
    x = 0
    while U > sum:
        x, sum = x + 1, sum + probability(x, sig, c)
    return x


def rec_e_regev(x, q):
    x = x.list()
    tab = []
    for y in x:
        y = int(y)
        if y > (q / 4) and y <= (3 * q / 4):
            tab.append(1)
        else:
            tab.append(0)
    return tab


# test parameters
c = 0
sig = 8 / sqrt(2 * pi)
N = 1024
q = 12289


def e_regev(N, q, sig, c):
    Z_q = IntegerModRing(q)
    Z. < x >= ZZ[]
    Rq. < x > = Z_q[]
    R_q = Rq.quo(x ^ N + 1, 'x')

    # s in Rq -private key , a in Rq ,e - a disrupt factor
    sA, eA = [], []
    sB, eB = [], []
    for x in range(0, N):
        eA.append(generator(round(sig), c))
        sA.append(generator(round(sig), c))
        eB.append(generator(round(sig), c))
        sB.append(generator(round(sig), c))
    sA = R_q(sA)
    eA = R_q(eA)

    a = R_q.random_element()

    eB = R_q(eB)
    sB = R_q(sB)

    tA = a * sA + eA
    tB = a * sB + eB

    kA = rec_e_regev(tA * sB, q)
    kB = rec_e_regev(tB * sA, q)
    return kA, kB


def test_regev(n, N, q, sig, c):
    negBits = 0
    for x in range(n):
        kA, kB = e_regev(N, q, sig, c)
        for y in range(N):
            if kA[y] != kB[y]:
                negBits += 1

    return negBits / (n * N)

