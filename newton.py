
import math
import re

pi = 3.14159265358979323846264338327950
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
def cos(x):
    x = x % (2 * pi) 
    c=1
    for i in range(1,32):
        c=c+(((-1)**i)*x**(i*2)/factorial(i*2))
    return c
def Cos(z):
    jz=1j*z
    return complex((complex(e**jz)+e**complex(-jz))/2)
def Sin(z):
    jz=1j*z
    return complex((complex(e**jz)-e**complex(-jz))/2j)
def Tan(z):
    return complex(Sin(z)/Cos(z))
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

def exponential(base,power):
    return e**(power*ln(base))
def log(base, arg):
    return ln(arg)/ln(base)

def polynomial_division(dividend, divisor):
    """
    Perform polynomial division on two polynomials with complex coefficients.
    
    Args:
    dividend (list): The dividend polynomial coefficients (highest degree first).
    divisor (list): The divisor polynomial coefficients (highest degree first).
    
    Returns:
    tuple: (quotient, remainder) where both are lists of coefficients.
    """
    # Ensure the divisor is not the zero polynomial
    if not any(divisor):
        raise ValueError("The divisor polynomial cannot be zero.")
    
    # Initialize quotient and remainder
    quotient = [0] * (len(dividend) - len(divisor) + 1)
    remainder = dividend[:]
    
    # Perform the division
    for i in range(len(dividend) - len(divisor) + 1):
        # Calculate the leading term of the quotient
        leading_term = remainder[i] / divisor[0]
        quotient[i] = leading_term
        
        # Subtract the current term times the divisor from the remainder
        for j in range(len(divisor)):
            remainder[i + j] -= leading_term * divisor[j]
    
    # Remove leading zeros from quotient and remainder
    while quotient and abs(quotient[0]) == 0:
        quotient.pop(0)
    while remainder and abs(remainder[0]) == 0:
        remainder.pop(0)
    return quotient, remainder
def compose_function(function: str):
    return lambda x: eval(function.replace('x', str(x)))
def compose_function(function: str):
    return lambda x: eval(function.replace('x', str(x)))
def derivative(function: str):
    def parse(function:str):
        return function.split('+')
    def power_rule():
def power_rule(n:str,type:str='func'): #formula for combined operations with kx^n
    def parse_polynomial(expr):
        pattern = r'[+-]?\d*x(?:\^\d+)?'
        terms = re.findall(pattern, expr)
        parsed_terms = []
        for term in terms:
            if 'x' in term:
                if '^' in term:
                    coeff, power = term.split('x^')
                    coeff = float(coeff) if coeff and coeff not in '+-' else float(coeff + '1')
                    power = float(power)
                else:
                    coeff = term.replace('x', '')
                    coeff = float(coeff) if coeff and coeff not in '+-' else float(coeff + '1')
                    power = 1
            else:
                coeff = float(term)
                power = 0
            parsed_terms.append((coeff, power))
        return parsed_terms
    
    def derivative_function(parsed_terms):
        def derivative(x):
            result = 0
            for coeff, power in parsed_terms:
                if power > 0:
                    result += coeff * power * (x ** (power - 1))
            return result
        if type == 'str':
            terms = []
            for coeff, power in parsed_terms:
                if power > 0:
                    new_coeff = coeff * power
                    new_power = power - 1
                    if new_power == 0:
                        terms.append(f"{new_coeff}")
                    elif new_power == 1:
                        terms.append(f"{new_coeff}x")
                    else:
                        terms.append(f"{new_coeff}x^{new_power}")
            return ' + '.join(terms).replace('+ -', '- ')
        else:
            return derivative
    
    def create_derivative_function(expr_str):
        if expr_str[0] not in '+-':
            expr_str = '+' + expr_str
        parsed_terms = parse_polynomial(expr_str)
        return derivative_function(parsed_terms)
    
    return create_derivative_function(n)

def exponential_rule(x,type:str='func'):
    def parse_string(s):
        pattern = r'(\d+)\*([0-9eE])\^([a-zA-Z])'
        match = re.match(pattern, s)
        number = int(match.group(1))  # The arbitrary length number
        one_digit = match.group(2)  # The one-digit number
        letter = match.group(3)  # The letter
        return number, one_digit, letter
    def derivative_function(parsed_terms):
        def derivative(x):
            if parsed_terms[1]=='e':
                return parsed_terms[0]*(e**x)
            else:
                return parsed_terms[0]*(float(parsed_terms[1])**x)*ln(float(parsed_terms[1]))
        if type=='str':
            if parsed_terms[1]!='e':
                return f'{parsed_terms[0]}ln({parsed_terms[1]}){parsed_terms[1]}^{parsed_terms[2]}'
            else:
                return f'{parsed_terms[0]}*{parsed_terms[1]}^{parsed_terms[2]}'
        
        return derivative
    return derivative_function(parse_string(x))





def cubic_equation(polynomial,guess:complex):
    answers=[]
    def parse_polynomial(poly):
        poly = poly.replace(' ', '')
        pattern = r'([+-]?\d*)x\^(\d+)|([+-]?\d*)x|([+-]?\d+)'
        terms = re.findall(pattern, poly)
        coefficients = {3: 1, 2: 0, 1: 0, 0: 0}
        for term in terms:
            # Handle the case of x^n
            if term[0] and term[1]:  # Match x^n
                coeff = term[0]
                if coeff == '' or coeff == '+':
                    coeff = 1
                elif coeff == '-':
                    coeff = -1
                else:
                    coeff = int(coeff)
                power = int(term[1])
            elif term[2]:  # Match x
                coeff = term[2]
                if coeff == '' or coeff == '+':
                    coeff = 1
                elif coeff == '-':
                    coeff = -1
                else:
                    coeff = int(coeff)
                power = 1
            else:  # Match constant
                coeff = term[3]
                if coeff == '':
                    coeff = 0
                else:
                    coeff = int(coeff)
                power = 0
            if power in coefficients:
                coefficients[power] += coeff
            else:
                coefficients[power] = coeff
        return coefficients
    def sol(parsed_terms,guess):
        for i in parsed_terms.values():
            i=i/parsed_terms[3]
        while abs(guess**3+(parsed_terms[2]*guess**2+guess*parsed_terms[1]+parsed_terms[0])/parsed_terms[3])>1e-18:
            if guess==guess-(guess**3+(parsed_terms[2]*guess**2+guess*parsed_terms[1]+parsed_terms[0])/parsed_terms[3])/(3*guess**2+(2*parsed_terms[2]*guess+parsed_terms[1])/parsed_terms[3]):
                break
            guess=guess-(guess**3+(parsed_terms[2]*guess**2+guess*parsed_terms[1]+parsed_terms[0])/parsed_terms[3])/(3*guess**2+(2*parsed_terms[2]*guess+parsed_terms[1])/parsed_terms[3])
            if abs(guess**3+(parsed_terms[2]*guess**2+guess*parsed_terms[1]+parsed_terms[0])/parsed_terms[3])<1e-12:
                print(guess, guess**3+(parsed_terms[2]*guess**2+guess*parsed_terms[1]+parsed_terms[0])/parsed_terms[3])
        answers.append(guess)
        return guess
    def divide(parsed_terms, guess):
        x=''
        polynomial=polynomial_division([i for i in parsed_terms.values()],[1,-guess])
        for i in polynomial[0]:
            x+=str(i)+'*x^'+str(2-polynomial[0].index(i))+'+'
        x=x.replace('x^1','x')
        x=x.replace('x^0','')
        return x[:-2]
    for i in range(3):
        c=parse_polynomial(polynomial)
        s=sol(c,guess)
        polynomial=divide(c,s)
    # return sol(parse_polynomial(polynomial),guess)
    return answers
# print(cubic_equation('x^3+5x^2-7x+12',complex(6,1))) #works however (obliously) founds only 1 root each time, therefore requires new guess for approximating new root. 

# input()

# c=complex(0.011,0.001)
# for i in range(5000):
#     c=c-(48*c*(c+1)**60-(c+1)**60+1)/(48*60*c*(c+1)**59-60*(c+1)**59)
#     # print(c,end=' ')
#     if abs(48*c*(c+1)**60-(c+1)**60+1)<1e2000:
#         print(48*c*(c+1)**60-(c+1)**60+1)
#         # break
# input()

# c=complex(1,1)
# for i in range(2000):
#     if c-(7+4*Sin(c)*Cos(c)+1.5*(Tan(c)+Cos(c)/Sin(c)))/(4*Cos(2*c)+3/(2*Cos(c)**2)-3/(2*Sin(c)**2))==c:
#         break
#     c=c-(7+4*Sin(c)*Cos(c)+1.5*(Tan(c)+Cos(c)/Sin(c)))/(4*Cos(2*c)+3/(2*Cos(c)**2)-3/(2*Sin(c)**2))
#     if abs(7+4*Sin(c)*Cos(c)+1.5*(Tan(c)+Cos(c)/Sin(c)))<1e-18:
#         print(c,end=' ')
#         print(7+4*Sin(c)*Cos(c)+1.5*(Tan(c)+Cos(c)/Sin(c)))
# input()

# c=float(input())
# for i in range(2000):
#     c=c-(7+4*sin(c)*cos(c)+1.5*(tan(c)+cos(c)/sin(c)))/(4*cos(2*c)+3/(2*cos(c)**2)-3/(2*sin(c)**2))
#     print(c)
# print(7+4*sin(c)*cos(c)+1.5*(tan(c)+cos(c)/sin(c)))
# input()