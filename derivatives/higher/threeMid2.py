from function import f

def threeMid2(x,h):
    return (1)/(h**2)*(f(x-h) - 2*f(x) + f(x+h))

print(threeMid2(5,.001))