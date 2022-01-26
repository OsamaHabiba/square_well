from pylab import *
import sys
from scipy.integrate import odeint
from scipy.optimize import brentq
from numpy import linspace, zeros, array
b = 2
v0 = 20 #potential outside the well
n = 100 #steps taken
E = 0 #eigenvalue of energy

def v(x):
    #potential function where the width of the well is 1
    #can be changed to any different shape to find different solution
    if x<1:
        return 0 #square well
    else:
        return v0

def se(y,x):
    #using x as time here
    g0 = y[1]
    g1 = -2*(E-v(x))*y[0]
    return array([g0, g1])

def final_val(energy):
    #calclate psi for this value of energy
    global y
    global E
    E = energy
    y = odeint(se, y0, x)
    return y[-1,0]

y = zeros([n,2])
y0 = array([1,0])
x = linspace(0, b, n)
#sys.argv is used to input search limits from the command line
E1 = float(sys.argv[1]) 
E2 = float(sys.argv[2])

answer = brentq(final_val, E1, E2)

print('eigenvalue for at:', answer)

plot(x,y[0:])
xlabel('position')
show()
