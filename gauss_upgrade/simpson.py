from lagrange import lagrange

def simpson(k,a,b,c, roots,n):
    return 1/3*((lagrange(n,k,a,roots)) + 4*(lagrange(n,k,b,roots)) + (lagrange(n,k,c,roots)))