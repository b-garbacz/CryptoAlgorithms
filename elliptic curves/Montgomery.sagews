#Implementation in sage-math

class Montgomery(object):
    def __init__(self,p,A,B):
        self.A = A #parameter A of Montgomery curve
        self.B = B #parameter B of Montgomery curve
        self.p = GF(p) # Finite field
        self.infinity = (None,None) # neutral point - Point in infinity

    #Method which one add point
    def add_point(self, xp, yp):
        try:
            if self.p( self.B * yp**2 )  == self.p(xp*(xp**2 + self.A*xp + 1)):
                self.point =  (self.p(xp), self.p(yp))
                return self.point
        except: print(" The point doesn't belong to the curve")


    # Points adding P(xp,yp) + Q(xq,yq) = Z(xz,yz)
    def add(self, P, Q):

        if P[0] == Q[0]  and P[1] == self.p(-Q[1]):   # If P=~Q then P+Q =Q+P = inf
            return self.infinity

        if P != self.infinity and Q != self.infinity: #If points are not in infinites then add them

            if P != Q:
                lambdaa = self.p((Q[1] - P[1]) / (Q[0] - P[0]))

            elif P == Q:
                lambdaa = self.p((3 * P[0]**2 + 2 * self.A * P[0] + 1) / (2 * self.B * P[1]))


            x = self.p(self.B * lambdaa**2 - (P[0] + Q[0]) - self.A)
            y = self.p(lambdaa  * (P[0] - x) - P[1])
            return x, y

        if P == self.infinity: #If point P is in infinity then return Q, because inf + Q = Q
            return Q

        if Q == self.infinity: #If point Q is in infinity then return P, because inf + P = Q
            return P


    #Mongomery Ladder
    def ladder(self, k, pkt):
        R0,R1 = self.infinity , pkt
        k = bin(k)[2:]
        for i in range(0,len(k)):
            if k[i] == "0":
                R1 = self.add(R1,R0)
                R0 = self.add(R0,R0)

            else:
                R0 = self.add(R0,R1)
                R1 = self.add(R1,R1)

        return R0




if __name__ == '__main__':
    p = 1099511627791
    A = 282986314544
    B = 810060215213
    xp = 712508459485
    yp = 647572200242
    r = 274878126563
    k = 4


    test = Montgomery(p,A,B)
    pkt1 = test.add_point(xp,yp)



    #Parameters of Montogmery curve: p, A, B, point P, ord r
    print("Parameters of the curve", "\np=", p,"\nA=",A,"\nB=",B,"\nord r=",r)

    xd = test.ladder(r,pkt1)

    #Ladder: point P, multiplicity of l and  result  Q = [l]P

    l1 = 218685976655
    wynik1 = test.ladder(l1,pkt1)
    print("\nParameters of the curve:","\nPoint P =",pkt1,"\ntimes l =",l1, "\nresult Q=[l]P =",wynik1)

    l2 = 205880727108
    wynik2 = test.ladder(l2,pkt1)
    print("\nParameters of the curve:","\nPoint  P =",pkt1,"\ntimes l =",l2, "\nresult Q=[l]P =",wynik2)

    l3 = 32581416758
    wynik3 = test.ladder(l3,pkt1)
    print("\nParameters of the curve:","\nPoint  P =",pkt1,"\ntimes l =",l3, "\nresult Q=[l]P =",wynik3)

    l4 = 133460278974
    wynik4 = test.ladder(l4,pkt1)
    print("\nParameters of the curve:","\nPoint  P =",pkt1,"\ntimes l =",l4, "\nresult Q=[l]P =",wynik4)

    l5 = 176382309228
    wynik5 = test.ladder(l5,pkt1)
    print("\nParameters of the curve:","\nPoint  P =",pkt1,"\ntimes l =",l5, "\nresult Q=[l]P =",wynik5)

    print("\n verification of r[P] = infinity = (None,None) ")
    print(test.ladder(r,pkt1))






