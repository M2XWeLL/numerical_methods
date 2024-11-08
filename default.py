pi = 3.14159265358979323846264338
def factor(num):
  l=[1]
  for i in range(2,num//2+1):
    while num//i!=0 and num-i>=i and num%i==0 :
      num=num//i
      l.append(i)
  l.append(num)
  return l
def factorial(x):
    c=1
    for i in range(x):
        c=c*(x-i)
    return c
def exp(x):
    c=1
    for i in range(1,32):
        c+=(x**i)/factorial(i)
    return c
e=exp(1)
def root(root,num):
    def func(x):
        return x**root-num
    def derivative(x):
        return root*x**(root-1)
    c=num/2
    epsilon=1e-12
    while abs(func(c))>epsilon:
        c=c-(func(c)/derivative(c))
    return c
def divide(parsed_terms, guess):
    l = parsed_terms
    l2 = []
    x1 = guess
    for i in range(len(l)-1):    
        l[i+1] = l[i+1] + l[i] * x1
        l2.append(l[i])
    return l2
def ln(arg):
    c=0
    while arg>e:
        arg=arg/e
        c+=1
    
    def f(x):
        return e**x-arg
    def f_prime(x):
        return e**x
    guess=arg-1
    while abs(e**guess-arg)>1e-18:
        if guess-f(guess)/f_prime(guess)==guess:
            break
        guess=guess-f(guess)/f_prime(guess)
    return guess+c
# def Ln(z):
#     a,b=complex(z)
#     r=root(2,(a**2+b**2))

#     return ln(abs(r))+1j*
def exponential(base,power):
    return e**(power*ln(base))
def log(base, arg):
    return ln(arg)/ln(base)