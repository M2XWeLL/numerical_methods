import re
import math,random
# def parse_polynomial(poly_str):

#     poly_str = poly_str.replace(' ', '')
#     if not poly_str.startswith(('+', '-')):
#         poly_str = '+' + poly_str
#     # term_pattern = re.compile(r'([+-]?[\d.]*)(x(?:\^(\d+))?)?')
#     term_pattern_1 = re.compile(r'(?=[+-])')

#     terms = term_pattern_1.split(poly_str)
#     terms.remove('')
    
#     d={3:0,2:0,1:0,0:0}
#     for i in terms:
#         temp=i.split('*')
#         coeff=temp[0]
#         if len(temp)==1:
#             d[0]=float(coeff)
#             continue
#         else:
#             power=temp[1].split('^')
#             if len(power)==1:
#                 d[1]=float(coeff)
#             else:
#                 d[int(power[1])]=float(coeff)

#             print(temp,coeff,power)
#     return d
def parse_polynomial(polynomial):
    # Regular expression pattern to match terms in the polynomial
    term_pattern = re.compile(r'([+-]?\s*\d*\.?\d*(?:e[+-]?\d+)?(?:\s*[+-]\s*\d*\.?\d*(?:e[+-]?\d+)?j)?)\s*\*\s*x\^(\d+)')
    constant_pattern = re.compile(r'([+-]?\s*\d*\.?\d*(?:e[+-]?\d+)?(?:\s*[+-]\s*\d*\.?\d*(?:e[+-]?\d+)?j)?)$')
    linear_pattern = re.compile(r'([+-]?\s*\d*\.?\d*(?:e[+-]?\d+)?(?:\s*[+-]\s*\d*\.?\d*(?:e[+-]?\d+)?j)?)\s*\*\s*x\b')

    # Find all terms with x^power
    terms = term_pattern.findall(polynomial)
    constants = constant_pattern.findall(polynomial)
    linears = linear_pattern.findall(polynomial)
    
    # Dictionary to hold the coefficients with their corresponding powers
    coeff_dict = {}

    # Function to clean and convert to complex
    def to_complex(coeff):
        return complex(re.sub(r'\s+', '', coeff))
    
    # Process the matched terms
    for term in terms:
        coefficient = to_complex(term[0])
        power = int(term[1])
        coeff_dict[power] = coefficient

    # Process the linear term
    for linear in linears:
        coefficient = to_complex(linear)
        coeff_dict[1] = coefficient

    # Process the constant term
    for constant in constants:
        coefficient = to_complex(constant)
        coeff_dict[0] = coefficient

    # Return the dictionary with coefficients and powers
    return coeff_dict

# Example polynomial
# polynomial = '1.0*x^2-(0.6947420088993796+1.181278741780463j)*x+1.8780859247119785'
# coefficients = parse_polynomial(polynomial)
# print(coefficients)
def split_expression(expression):
    # Регулярное выражение для поиска математических функций, экспонент, переменных, чисел и операторов
    pattern = r'([+-]?\b(?:ln|log|sin|cos|tan|sqrt|exp)\b\([\w\^+\-*/\.]+\)|[+-]?e\^\w+|[+-]?\d*\.?\d*\w*(?:\^\d+)?|[+-]?\d+)'
    
    # Используем re.findall для поиска всех совпадений
    result = re.findall(pattern, expression)
    
    # Убираем пустые строки, которые могут возникнуть
    result = [term for term in result if term]
    
    return result


expression = "x"
split_result = split_expression(expression)
print(split_result)