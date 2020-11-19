from f import f
import numpy as np

def trap2D_pt2(xmin, xmax, ymin, ymax, nx, ny, A):

    dS = ((xmax-xmin)/(nx-1)) * ((ymax-ymin)/(ny-1))

    A_Internal = A[1:-1, 1:-1]
    (A_u, A_d, A_l, A_r) = (A[0, 1:-1], A[-1, 1:-1], A[1:-1, 0], A[1:-1, -1])
    (A_ul, A_ur, A_dl, A_dr) = (A[0, 0], A[0, -1], A[-1, 0], A[-1, -1])
    return dS * (np.sum(A_Internal)\
                + 0.5 * (np.sum(A_u) + np.sum(A_d) + np.sum(A_l) + np.sum(A_r))\
                + 0.25 * (A_ul + A_ur + A_dl + A_dr))

x_min,x_max,n_points_x = (0,1,50)
y_min,y_max,n_points_y = (0,5,50)
x = np.linspace(x_min,x_max,n_points_x)
y = np.linspace(y_min,y_max,n_points_y)

zz = f(x.reshape(-1,1),y.reshape(1,-1))

print(trap2D_pt2(x_min, x_max, y_min, y_max, n_points_x, n_points_y, zz))