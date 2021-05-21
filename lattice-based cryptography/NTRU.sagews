import random
Zx.<x> = ZZ[]

def randTrin(d1,d2,N):
    Z.<x>=ZZ[]
    R = Z.quo(x^N-1,'x')
    n=N-d1-d2

    poly_trin=[]
    for i in range(0,d1):
        poly_trin.append(1)
    for i in range(0,d2):
        poly_trin.append(-1)
    for i in range(0,n):
        poly_trin.append(0)

    random.shuffle(poly_trin)
    return R(poly_trin)

def genMSG(p,N):
    msg=[]
    Z.<x>=ZZ[]
    R = Z.quo(x^N-1,'x')

    interval  = int(1/2*p)
    for x in range(N):
        msg.append(randint(-interval , interval ))

    return R(msg)

def Central_lift(N,f,q):
    Z.<x>=ZZ[]
    R = Z.quo(x^N-1,'x')

    out=[]
    for i in f:
        if int(i) >=0 and int(i) <= q/2:
            out.append(int(i))
        if int(i) > q/2 and int(i) < q:
            out.append(int(i)-q)
    return R(out)



def gen(N,p,q,d):
    #defining algebraic structures
    Z_q = IntegerModRing(q)
    Z_p = IntegerModRing(p)
    Z.<x>=ZZ[]
    R = Z.quo(x^N-1,'x')
    #structure of Rq
    Rq.<x> = Z_q[]
    R_q = Rq.quo(x^N-1,'x')
    #structure of Rp
    Rp.<x> = Z_p[]
    R_p = Rp.quo(x^N-1,'x')

    #generating a random trinary polynomial f
    f = randTrin(d+1,d,N)
    g = randTrin(d,d,N)

    #"putting"? the polynomial mod q and mod p
    fq = R_q(f)
    fp = R_p(f)

    #check if fq and fp are both contained
    while True:
        fq = R_q(f)
        fp = R_p(f)
        if fq.is_unit() == True and fp.is_unit() == True: break

    pub = p * fq^(-1) * g
    priv = (fq, fp^(-1))
    if fq*fq^(-1) == 1: return priv,pub
    else: False

def enc(msg,N,pub,d,q):
    Z_q = IntegerModRing(q)
    Z.<x>=ZZ[]
    Rq.<x> = Z_q[]
    R_q=Rq.quo(x^N-1,'x')

    r=randTrin(d,d,N)
    e=r*pub+msg
    e = R_q(e)
    return e

def dec(e,N,priv,q):
    Z_p = IntegerModRing(p)
    Rp.<x> = Z_p[]
    R_p = Rp.quo(x^N-1,'x')

    aq=e*priv[0]
    a=Central_lift(N,aq,q)
    ap=R_p(a)
    mp=ap*priv[1]
    m=Central_lift(N,mp,p)
    return m

N,p,q,d=7,3,41,2 # Correct parameters
#N,p,q,d = 251,2,239,72 #Wrong parameters
def emulatorNTRU(N,p,q,d):

    priv,pub = gen(N,p,q,d)
    #print("PRIV=",priv,"\nPUB=",pub)
    msg=genMSG(p,N)
    #print("msg=",msg)
    e=enc(msg,N,pub,d,q)
    #print("e=",e)
    decmsg=dec(e,N,priv,q)
    #print("decmsg=",decmsg)
    if msg==decmsg: return True
    else: return False
emulatorNTRU(N,p,q,d)









