import numpy as np
import math

#Baby-step giant-step
def xgcd(x, N):
    if x > N:
        return False, False, False
    X, Y, R, S = 1, 0, 0, 1
    while N != 0:
        C = x % N
        Q = math.floor(x / N)
        x, N = N, C
        Rp, Sp = R, S
        R = X - Q * R
        S = Y - Q * S
        X, Y = Rp, Sp
    d = x
    u = X
    v = Y
    return d, u, v


def modinv(x, N):
    d, u, v = xgcd(x, N)
    if d != 1:
        return False
    return u % N


def shanks(p, g, h):
    a, b, m = 0, 0, int(np.ceil(math.sqrt(p - 1)))
    disti = {}
    for j in range(0, m):
        disti[pow(g, j, p)] = j
    disti = dict(sorted(disti.items()))
    for i in range(0, m):
        exp = pow(g, i * m, p)  # exp = g^{i*m}
        inv_exp = modinv(exp, p)  # modular inverse of exp, exp =g{-i*m}

        if not inv_exp:
            continue
        calc = (h * inv_exp % p)

        if calc in disti:
            a = i
            b = disti[calc]
            break
    return a * m + b
