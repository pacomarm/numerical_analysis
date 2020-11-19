from function import f

def threeMid(x,h):
    return 1/(2*h)*(f(x+h) - f(x-h))