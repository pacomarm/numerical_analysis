from f import f 

def simp2D(a,b,c,d,n,m):
    h = (b-a)/n 
    J1 = 0
    J2 = 0 
    J3 = 0
    for i in range(0,n):
        x = a + i*h
        HX = (d-c)/m
        K1 = f(x,c) + f(x,d)
        K2 = 0;
        K3 = 0;
        for j in range(1, m-1):
            y = c + j*HX
            Q = f(x,y)
            if (j%2==0):
                K2 = K2 + Q
            else:
                K3 = K3 + Q
        L = (K1 + 2*K2 + 4*K3)*HX/3
        if(i == 0 or i == n):
            J1 = J1 + L
        else: 
            if(i%2 == 0):
                J2 = J2 + L
            else:
                J3 = J3 + L
    J = h * ( J1 + 2*J2 + 4*J3)/3
    return J

print(simp2D(0,1,0,5,1000,1000))
