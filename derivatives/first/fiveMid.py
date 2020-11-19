from function import f

def fiveMid(x,h):
    return 1/(12*h)*(f(x-2*h) - 8*f(x-h) + 8*f(x+h) - f(x+2*h))
