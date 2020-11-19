from simp import simp
n= 1000
def simpComp(a,b):
    i = a
    h = (b-a)/n
    sum = 0
    while(i<=b):
        if(i+h<=b):
            sum+= simp(i, i+h)
        i+=h
    return sum

print(simpComp(3,4))

