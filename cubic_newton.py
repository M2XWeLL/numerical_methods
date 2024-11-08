import re
from collections import defaultdict
# def polynomial_division(dividend, divisor):
#     quotient = []
#     remainder = dividend[:]
#     divisor_degree = len(divisor) - 1
#     divisor_leading_coefficient = divisor[0]
    
#     while len(remainder) >= len(divisor):
#         leading_term = remainder[0] / divisor_leading_coefficient
#         quotient.append(leading_term)
#         for i in range(len(divisor)):
#             remainder[i] -= leading_term * divisor[i]
#         remainder.pop(0)
    
#     return quotient, remainder

# def divide(parsed_terms, guess):
#     dividend = [parsed_terms[3], parsed_terms[2], parsed_terms[1], parsed_terms[0]]
#     quotient, remainder = polynomial_division(dividend, [1, -guess])
#     x = ''
#     for i in range(len(quotient)):
#         coeff = quotient[i]
#         power = len(quotient) - 1 - i
#         if coeff != 0:
#             x += f'{coeff:+}*x^{power} '
#     x = x.replace('x^1', 'x')
#     x = x.replace('x^0', '')
#     return x.replace(' ','')[:-1]
answers = []




def sol(parsed_terms, guess):
    # Ensure the leading coefficient is non-zero
    if parsed_terms[3] == 0:
        raise ValueError("The leading coefficient (coefficient of x^3) cannot be zero.")
    
    # Normalize coefficients
    norm_coeffs = {k: v / parsed_terms[3] for k, v in parsed_terms.items()}
    
    while abs(guess**3 + (norm_coeffs[2] * guess**2 + norm_coeffs[1] * guess + norm_coeffs[0])) > 1e-18:
        new_guess = guess - (guess**3 + (norm_coeffs[2] * guess**2 + norm_coeffs[1] * guess + norm_coeffs[0])) / (3 * guess**2 + 2 * norm_coeffs[2] * guess + norm_coeffs[1])
        if guess == new_guess:
            break
        guess = new_guess
        
        # if abs(guess**3 + (norm_coeffs[2] * guess**2 + norm_coeffs[1] * guess + norm_coeffs[0])) < 1e-12:
        #     print(guess, guess**3 + (norm_coeffs[2] * guess**2 + norm_coeffs[1] * guess + norm_coeffs[0]))
    
    answers.append(guess)
    return guess


def divide(parsed_terms, guess):
    l = parsed_terms
    l2 = []
    x1 = guess
    for i in range(len(l)-1):    
        l[i+1] = l[i+1] + l[i] * x1
        l2.append(l[i])
    return l2
def cubic_equation_solver(polynomial, guess):
    for i in range(2):
        c = parse_polynomial(polynomial)
        print(c)
        s = sol(c, guess)
        polynomial = divide(c, s)
        print(polynomial)
    return answers

# polynomial = 'x^3 + 5x^2 - 7x + 12'
polynomial= '1.0*x^2-(0.6947420088993796+1.181278741780463j)*x+1.8780859247119785'
guess = 1.0
# print(cubic_equation_solver(polynomial, guess))
print(parse_polynomial(polynomial))