#!/bin/python

from math import sin
from numpy import arange
from pylab import plot,xlabel,ylabel,show

def f(x,t):
    return -x**3 + sin(t)

a = 0.0           #iniciem l'interval
b = 10.0          #finalitzem l'interval
N = 1000          #número de passos
h = (b-a)/N       #tamany d'un interval
x = 0.0           #condicions inicials

puntst = arange(a,b,h)
puntsx = []

for t in puntst:
    puntsx.append(x)
    x += h*f(x,t)

plot(puntst,puntsx)
xlabel("t")
ylabel("x(t)")
show()
