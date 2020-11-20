def lagrange(n,k,x,X):
    I = 1
    for i in range(n):
        if i!=k:
            I = I * ((x-X[i])/(X[k]-X[i]))
    return I