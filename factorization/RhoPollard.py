export PYTHONPATH="${PYTHONPATH}:C:\Users\barti\CryptoAlgorithms
from random import *
#Pollard's rho algorithm
def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

def fact_pollard(n):
    x_0=2        #basic values (might be random)
    y_0=2
    a=1
    fun = lambda x_0: ((x_0**2) + a) % n  #creating polynomial (x_0)^2 + 1 (mod n)
    d=1
    while (d == 1): #superposition for f (x_0) and f (f (y_0))
        x_0 = fun(x_0)

        y_0 = fun( fun(y_0) )

        d =  gcd( abs(x_0 - y_0) , n ) #Do it while until  |x_0 -y_0| it is relatively prime with n
    if 1<d<n: return [d,int(n/d)]




def fact_pollard_2(n, y):
    x_0=2         #basic values (might be random)
    y_0=2
    a=1
    while(y > 0):
        fun = lambda x_0: ((x_0**2) + a) % n #creating polynomial (x_0)^2 + 1 (mod n)
        d=1
        while (d == 1):   #superposition for f (x_0) and f (f (y_0))
            x_0 = fun(x_0)

            y_0 = fun( fun(y_0) )

            d =  gcd( abs(x_0 - y_0) , n ) #Do it while until  |x_0 -y_0| it is relatively prime with n
        if 1<d<n:
            return [d,int(n/d)]
        y = y - 1       #If  dividers of n cannot be found, generate new values for a,x_0 and y_0. No more than y times
        a   = randint(1, n)
        x_0 = randint(2, n)
        y_0 = randint(2, n)

