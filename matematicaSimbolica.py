from sympy import *
import math


T = 2 * math.pi


x, n = symbols("x n")

a0 = Integral (x, x).doit() /T
an = Integral (x * cos(2 * math.pi/T*x),x).doit() *2.0/T
bn = Integral (x * sin(2 * math.pi/T*x),x).doit() *2.0/T

def f(xi, a0, an, bn, x , N):
    s = a0.evalf(subs = {x: xi})
    for ni in range(1, N + 1):
        s += an.evalf(subs = {x: xi, n:ni}) * math.cos(2 * ni * math.pi / T * xi)
        s += bn.evalf(subs = {x: xi, n:ni}) * math.sin(2 * ni * math.pi / T * xi)
        return s

def linspace(a, b, c):
    if n <= 1:
        return [(a+b) / 2.0]

       vec  = []
       delta = (b-a)/ float(n-a)   


print (a0)
print (an)
print (bn)