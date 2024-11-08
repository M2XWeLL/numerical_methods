from trigonometry import *
import math
e=2.718281828
pi=22/7
def ceil(num):
    integer_part = int(num) 
    if num > integer_part: 
        return integer_part + 1
    return integer_part 

def gaussian_distribution(x):
    return e**(-(x**2))
def parabola(x):
    return x**2

def definite_integral(a,b,func):
    if a=='-inf':
        a=-10
    if b=='inf':
        b=10
    epsilon=1e-6
    n=ceil((b-a)/epsilon)
    dx=(b-a)/n
    counter=0
    for i in range(n):
        x_mid = a + (i + 0.5) * dx  # Midpoint of the interval
        counter += func(x_mid) * dx
        print(i,x_mid,counter)
    return counter

def fourier_transform(xi,func):
    def g(x):
        return func(x)*e**(-2j*pi*xi*x)
    return definite_integral('-inf','inf',g)
print(fourier_transform(1,sin))
