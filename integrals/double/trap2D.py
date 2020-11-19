from f import f

def trap2D(a,b,c,d):
    return (((b-a)*(d-c))/16)*(f(a,c)+f(a,d)+f(b,c)+f(b,d)+2*(f((a+b)/2,c)+f((a+b)/2,d)+f(a,(c+d)/2)+f(b,(c+d)/2))+ 4*f((a+b)/2,(c+d)/2))

print(trap2D(0,1,0,5))
