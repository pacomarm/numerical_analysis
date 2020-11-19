from f import f

def trapComp(f,a,b,Iold,k):
    if(k==1):
        Inew = (b-a)/2*(f(a)+f(b)) 
    else:
        n = 2**(k-2)
        h = (b-a)/n
        x = a + h/2
        sum = 0
        for i in range(n):
            sum+= f(n)
            x+=h
        Inew = (Iold + h*sum)/2
    return Inew

print(trapComp(f, 3,4,0,10))