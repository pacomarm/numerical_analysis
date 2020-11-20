from lagrange import lagrange

def simpson(k,a,b,c, roots):
    return 1/3*((lagrange(3,k,a,roots)) + 4*(lagrange(3,k,b,roots)) + (lagrange(3,k,c,roots)))