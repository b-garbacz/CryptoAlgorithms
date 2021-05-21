def genMatrix(n):
    rz_Matrix = 0
    while rz_Matrix != n : #Rand the matrix while ord != n
        Matrix = random_matrix(ZZ,n,n)
        rz_Matrix = Matrix.rank()

    return Matrix.transpose()



def RGL(b): #Gauss-Lagrange Reduction Algorithm
    b1=b[0]
    b2=b[1]
    if b2.norm()<b1.norm():
        pom=b2
        b2=b1
        b1=pom
    m=round(b1.dot_product(b2)/b1.dot_product(b1))
    A=matrix([b1,b2])
    while True:
        B=matrix([(-m,1),(1,0)])
        A=B*A
        m=round(A[0].dot_product(A[1])/(A[0].dot_product(A[0])))
        if m == 0:
            break
    return matrix((A[0],A[1]))



def gs(matrixlnz): #Gram–Schmidt process
    u = matrix(QQ, matrixlnz.nrows(),matrixlnz.ncols())
    u[0]=matrixlnz[0]
    for i in range(1,matrixlnz.nrows()):
        u[i] = matrixlnz[i]
        for j in range(0,i):
            mi = matrixlnz[i].dot_product(u[j])/u[j].dot_product(u[j])
            u[i] = u[i] - mi*u[j]
    return u


def LLL(b): #Lenstra–Lenstra–Lovász algorithm
    mi=matrix(QQ, b.nrows(),b.ncols())
    i=1

    while i < b.nrows():
        sum = vector(QQ, b.nrows())
        for j in range(i-1):
            mi[i,j] = b[i].dot_product(b[j])/b[j].dot_product(b[j])
            q = round(mi[i,j])
            sum += q*b[j]
        b[i] = b[i]-sum

        if pow(gs(b)[i].norm(),2) >=  (3/4 - pow(mi[i,i-1],2)) * pow(gs(b)[i-1].norm(),2):
            i+=1

        else:
            b.swap_rows(i,i-1)
            k=max(1,i-1)
    return b




