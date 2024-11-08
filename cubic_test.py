import re
answers = []
# print((-0.8333333333333333)**3+5*(-0.8333333333333333)**2-7*(-0.8333333333333333)+12)
def prep(parsed_terms):
    d={}
    if parsed_terms[0] == 0:
        raise ValueError("The leading coefficient (coefficient of x^3) cannot be zero.")
    for i in range(len(parsed_terms)):
        d[len(parsed_terms)- i-1] = parsed_terms[i]
    return d
def solve(parsed_terms, guess):
    def calc(guess):
        temp_result=0
        temp_result_derivative=0
        for key,value in parsed_terms.items():
            temp_result+=value*guess**key
            if key>0:
                temp_result_derivative+=value*key*guess**(key-1)
        return temp_result,temp_result_derivative
    print(parsed_terms)
    while abs(guess) > 1e-18:
        c=calc(guess)
        new_guess=guess-(c[0]/c[1])
        if guess == new_guess:
            print('end')
            return guess
        
        guess = new_guess
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
        c=prep(polynomial)
        s = solve(c, guess)
        answers.append(s)
        polynomial = divide(list(c.values()), s)
        print(polynomial)
        print(answers)
    return answers
polynomial=[1,5,-7,12]
# polynomial= [1.0,-(0.6947420088993796+1.181278741780463j),+1.8780859247119785] #'1.0*x^2-(0.6947420088993796+1.181278741780463j)*x+1.8780859247119785'
guess = 1.0
print(solve(prep([1, -1.3894840177987593, 1.8780859247119785]),guess))
# print(cubic_equation_solver(polynomial, guess))

