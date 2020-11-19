import numpy as np

degree = 3          # DEGREE OF POLYNOMIAL

coeff = []
points_integral = [-1,0,1]      # the points of the simpson integral (a,b,c)

root = np.array([-0.774658203125,0.0, 0.774658203125], float) #las raìces
y = np.array([1,4,1], float)

def lag_simp(xp):
    yp = 0
    print(np.prod((xp - root[root != root[0]])/(root[0] - root[root != root[0]])))

lag_simp(0)


