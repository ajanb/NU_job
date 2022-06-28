import numpy as np
import math
#from scipy.integrate import *
import scipy.optimize as optimize
from scipy.integrate import nquad
from scipy.integrate import dblquad
import matplotlib.pyplot as plt



#########################################

def contourplotV(w1, w2, h1, h2, dx, dy, alpha, function):
    
    xlist = np.linspace(w1, w2, 100)
    ylist = np.linspace(h1, h2, 100)
    X, Y = np.meshgrid(xlist, ylist)
    
    Z = np.zeros((100,100))
    for i in range(100):
        for j in range(100):
            Z[i,j] = function(ylist[i],xlist[j], dx, dy, alpha, r)
    
    
    
    
    fig,ax=plt.subplots(1,1)
    cp = ax.contourf(X, Y, Z)
    fig.colorbar(cp) # Add a colorbar to a plot
    ax.set_title('V distribution')
    plt.show()



def rotcoords(y, x, alpha):
    
    X = x * np.cos(-alpha) + y * np.sin(-alpha)
    Y = -y * np.sin(-alpha) + y * np.cos(-alpha)
    
    return (X, Y)



def getcoords(y, x, dx, dy, alpha, r):
    d = 2 * r 
    X, Y = rotcoords((y-dy), (x-dx), alpha)
    #dX, dY = rotcoords(dy, dx, alpha)
    
    #X = X - dX
    #Y = Y - dY
    
    X = np.abs(X  - X // d * d) - r
    Y = np.abs(Y  - Y // d * d) - r
    
    
    I = np.sqrt(X**2 + Y**2)
    
    
    return I


def function_V(y, x, dx, dy, alpha, r):
    v1=getcoords(y,x,0,0,0,r)
    #v1=getcoords(y,x,dx,dy,alpha,r)
    if v1>=r:
        v1 = 0
    
    v2=getcoords(y,x,dx,dy,alpha,r)
    if v2>=r:
        v2 = 0
    
    V = np.max([v1, v2])
    
    return V


def function_Al(y, x, dx, dy, alpha, r):
    
    R1=getcoords(y,x,0,0,0,r)
    #R1=getcoords(y,x,dx,dy,alpha,r)
    if (R1<r/3) or (R1>r):
        A1 = 1
    else:
        A1 = 0
    
    
    R2=getcoords(y,x,dx,dy,alpha,r)
    if (R2<r/3) or (R2>r):
        A2 = 1
    else:
        A2 = 0
    
    
    A = np.min([A1, A2])
    
    return A



def function_Ah(y, x, dx, dy, alpha, r):
    
    R1=getcoords(y,x,0,0,0,r)
    #R1=getcoords(y,x,dx,dy,alpha,r)
    if (R1<=r) and (R1>=2*r/3):
        A1 = 1
    else:
        A1 = 0
    
    
    R2=getcoords(y,x,dx,dy,alpha,r)
    if (R2<=r) and (R2>=2*r/3):
        A2 = 1
    else:
        A2 = 0
    
    
    A = np.max([A1, A2])
    
    return A


def intgrl_V(params):
    dx, dy, alpha = params
    r=0.5
    d = 2 * r
    
    w1 = 0 
    w2 = 3*d 
    h1 = 0 
    h2 = 3*d 
    
    # Integrate for V
    intgrl, abserr = dblquad(function_V, w1, w2, lambda x: h1, lambda x: h2, args=(dx, dy, alpha, r))

    # options = {'limit': 100}
    # intgrl, abserr = nquad(function_V, [[w1,w2],[h1,h2]], args=(dx, dy, alpha, r), opts=[options, options])
    # Take average of the integral over the area
    A = (w2 - w1) * (h2 - h1)
    return -intgrl/A


def intgrl_Al(params):
    dx, dy, alpha = params
    r=0.5
    d = 2 * r
    
    w1 = 0 
    w2 = 3*d 
    h1 = 0 
    h2 = 3*d 
    
    # Integrate for A_low
    intgrl, abserr = dblquad(function_Al, w1, w2, lambda x: h1, lambda x: h2, args=(dx, dy, alpha, r))
    
    # options = {'limit': 100}
    # intgrl, abserr = nquad(function_Al, [[w1,w2],[h1,h2]], args=(dx, dy, alpha, r), opts=[options, options])

    # Take average of the integral over the area
    A = (w2 - w1) * (h2 - h1)
    return intgrl/A


def intgrl_Ah(params):
    dx, dy, alpha = params
    r=0.5
    d = 2 * r
    
    w1 = 0 
    w2 = 3*d 
    h1 = 0 
    h2 = 3*d 
    
    # Integrate for A_low
    intgrl, abserr = dblquad(function_Ah, w1, w2, lambda x: h1, lambda x: h2, args=(dx, dy, alpha, r))

    # options = {'limit': 100}
    # intgrl, abserr = nquad(function_Ah, [[w1,w2],[h1,h2]], args=(dx, dy, alpha, r), opts=[options, options])
    
    # Take average of the integral over the area
    A = (w2 - w1) * (h2 - h1)
    return -intgrl/A


def optfun(params):
    return 1.9 * intgrl_V(params) + 7.6 * intgrl_Al(params) + intgrl_Ah(params) 



params=result.x 
print(-intgrl_V(params)) 
print(intgrl_Al(params))
print(-intgrl_Ah(params))


initial_guess = [0.25, 0.4, 0]
result = optimize.minimize(optfun, initial_guess)


if result.success:
    fitted_params = result.x
    print(fitted_params)
else:
    raise ValueError(result.message)


# Contour plot
#contourplotV(w1, w2, h1, h2, dx, dy, alpha, function_V)
#plt.close('all')


# Contour plot
#contourplotV(w1, w2, h1, h2, dx, dy, alpha, function_Al)
#plt.close('all')


# Contour plot
#contourplotV(w1, w2, h1, h2, dx, dy, alpha, function_Ah)
#plt.close('all')


