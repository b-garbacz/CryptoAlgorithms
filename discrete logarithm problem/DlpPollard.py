import math
from random import *

#Pollard's p − 1 algorithm

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

def power_mod(a, b, N):
    t = 1
    while(b > 0):
        if(b % 2 == 1):
            t = t * a % N
        a = a * a % N
        b = (b // 2)
    return t % N

def divisors(ord):
    divs = []
    i = 1
    while i <= ord:
        if ord % i == 0:
            divs.append(i)
        i += 1
    return divs

def order(g, p):
    ord = p-1
    divs = divisors(ord)
    for div in divs:
        if pow(g, div, p) == 1:
            return div

def gx(x_j, a_j, b_j, p, g, h, n):
    if (x_j % 3 == 0):
        x_j = x_j * x_j
        b_j = 2 * b_j
        a_j = 2 * a_j
    elif (x_j % 3 == 1):
        x_j = x_j * g
        a_j = a_j + 1
    elif (x_j % 3 == 2):
        x_j = x_j * h
        b_j = b_j + 1
    return x_j % p, a_j % n, b_j % n


def conditions(r1, r2, n):
    euclid_param = xgcd(r1, n)
    if (euclid_param[0] == 1):
        return (euclid_param[1] * r2) % n
    elif (r2 % euclid_param[0] == 0):
        return ((euclid_param[1] * r2) / euclid_param[0]) % n
    else:
        return 0


def walk(a_j, a_2j, b_j, b_2j, x_j, x_2j,p, g, h):
    a_j = randint(1, p - 1)
    a_2j = a_j
    b_j = randint(1, p - 1)
    b_2j = b_j
    x_j = (power_mod(g, a_j, p) * power_mod(h, b_j, p)) % p
    x_2j = x_j
    return a_j, a_2j, b_j, b_2j, x_j, x_2j

def Rho(p, g, h):
    # ord prime for g w Fp.
    n = order(g, p)

    x_j, a_j, b_j = 1, 0, 0
    x_2j, a_2j, b_2j = 1, 0, 0

    while (True):
        x_j, a_j, b_j = gx(x_j, a_j, b_j, p, g, h, n)
        x_2j, a_2j, b_2j = gx(x_2j, a_2j, b_2j, p, g, h, n)
        x_2j, a_2j, b_2j = gx(x_2j, a_2j, b_2j, p, g, h, n)
        if (x_2j == x_j):
            r = b_j - b_2j
            if r != 0:
                solution = conditions(r, a_2j - a_j, n)
                if (power_mod(g, solution, p) == h):
                    return solution
            else:
                a_j, a_2j, b_j, b_2j, x_j, x_2j = walk(a_j, a_2j, b_j, b_2j, x_j, x_2j, p, g, h)