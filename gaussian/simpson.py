from lagrange import lagrange

roots = [-0.774658203125, 0.0, 0.774658203125]

def simpson(k,a,b,c):
    return 1/3*((lagrange(3,k,a,roots)) + 4*(lagrange(3,k,b,roots)) + (lagrange(3,k,c,roots)))
