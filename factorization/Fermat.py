export PYTHONPATH="${PYTHONPATH}:C:\Users\barti\CryptoAlgorithms"
import math
#Fermat's factorization method
def fermat(n):
    t = math.floor(math.sqrt(n)) + 1
    x = (t**2) -n
    y=math.sqrt(x)
    while not y.is_integer():
        t = t + 1
        x = (t ** 2) - n
        y=math.sqrt(x)
    p = (t + y)
    q = (t - y)
    return t,y,p,q


