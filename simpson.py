 def simpson(a,b):
    h = (b-a)/2
    midPoint = (a+b)/2 
    return (h/3)*(f(a) + 4*f(midPoint) + f(b))