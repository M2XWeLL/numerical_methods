from default import *
def cos(x):
    x = x % (2 * pi) 
    c=1
    for i in range(1,32):
        c=c+(((-1)**i)*x**(i*2)/factorial(i*2))
    return c
def sin(x):
    x = x % (2 * pi) 
    c=x
    for i in range(1,32):
        c=c+(((-1)**i)*x**(i*2+1)/factorial(i*2+1))  
    return c 
def tan(x):
    if cos(x) == 0:
        raise ValueError("Undefined value for tan(x) when cos(x) is 0.")
    return sin(x)/cos(x)
def cot(x):
    return 1/tan(x)
def sec(x):
    return 1/cos(x)
def csc(x):
    1/sin(x)
def Cos(z):
    jz=1j*z
    return complex((complex(e**jz)+e**complex(-jz))/2)
def Sin(z):
    jz=1j*z
    return complex((complex(e**jz)-e**complex(-jz))/2j)
def Tan(z):
    return complex(Sin(z)/Cos(z))
def Cot(z):
    return complex(1/Tan(z))
def Sec(z):
    return complex(1/Cos(z))
def Csc(z):
    return complex(1/Sin(z))
def asin(x):
    c=0
    i=0
    while abs(sin(c)-x)>1e-4:
        c+=(factorial(2*i)*x**(2*i+1))/(((2**i*factorial(i))**2)*(2*i+1))
        i+=1
    return c

def sinh(z):
    return (e**z-e**(-z))/2
def cosh(z):
    return (e**z+e**(-z))/2
def tanh(z):
    return sinh(z)/cosh(z)
def coth(z):
    return 1/tan(z)
def sech(z):
    return 1/cosh(z)
def csch(z):
    return 1/sinh(z)

