
import re
num='1234567890'
letters='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
def divide(parsed_terms, guess):
    l = parsed_terms
    l2 = []
    x1 = guess
    for i in range(len(l)-1):    
        l[i+1] = l[i+1] + l[i] * x1
        l2.append(l[i])
    return l2
def exp(x):
    return 2.71**x
def numerical_derivative(a,func):
    epsilon=1e-12
    return (func(a + epsilon) - func(a - epsilon)) / (2 * epsilon)
def derivative(expression):
    def parse(expression):

        result=''
        i=0
        c=False
        while i<len(expression):
            if c and expression[i]=='+':
                result+=')'+expression[i]
            elif expression[i]=='-':
                result+='+('+expression[i]
                c=True
            else:
                result+=expression[i]
            i+=1
        if c:
            result+=')'
        new_result=[]
        i=0
        c=[False,0]
        while i<len(result):
            if i+1<len(result) and result[i] in letters and result[i+1]=='(':
                c=[True,i]
            elif result[i]==')' and c[0]==True:
                c=[False,i]
            else:
                c[0]=False
            if result[i]=='+' and c[0]==False:
                new_result.append(result[c[1]-1:i])
            i+=1
        return new_result
    def split_expression(expression):
        # Регулярное выражение для поиска математических функций, экспонент, переменных, чисел и операторов
        pattern = r'([+-]?\b(?:ln|log|sin|cos|tan|sqrt|exp)\b\([\w\^+\-*/\.]+\)|[+-]?e\^\w+|[+-]?\d*\.?\d*\w*(?:\^\d+)?|[+-]?\d+)'
        
        # Используем re.findall для поиска всех совпадений
        result = re.findall(pattern, expression)
        
        # Убираем пустые строки, которые могут возникнуть
        result = [term for term in result if term]
        
        return result
    def polynomial_derivative(expression):
        def parse(expression):
            expression += ' '  # Добавляем пробел в конец для корректной работы с последним символом
            result = []  # Список для сбора новой строки
            i = 0  # Индекс для обхода строки
            while i < len(expression):
                if expression[i] in num and (i + 1 < len(expression) and expression[i + 1] != 'x' and expression[i-1]!='^'):
                    # Если символ — это число и за ним не идёт 'x'
                    result.append(expression[i])
                    result.append('x^0')  # Вставляем 'x^0'
                elif expression[i] == 'x' and (i + 1 < len(expression) and expression[i + 1] != '^'):
                    # Если символ — это 'x', но за ним не идёт '^'
                    result.append(expression[i])
                    result.append('^1')  # Вставляем '^1'
                else:
                    # Просто добавляем символ в результат
                    result.append(expression[i])
                i += 1
            expression=''.join(result)
            pattern = r'[+-]?\d*x(?:\^\d+)?'
            terms = re.findall(pattern, expression)
            spl=[]
            for i in terms:
                spl.append(i.split('x'))
            for i, (x, y) in enumerate(spl):  
                z = y.replace('^', '')
                spl[i] = (x, z)
            return spl
    
        def der(coeff):
            c=[]
            for x,y in coeff:
                if int(y)!=0:
                    c.append((int(x)*int(y),int(y)-1))
            return c
        def repr(coeff):
            result=''
            for x,y in coeff:
                if str(x)[0]!='-':
                    x='+'+str(x)
                result+=str(x)+'x^'+str(y)
            result=result.replace('x^1','x')
            result=result.replace('x^0','')
            if result[0]=='+':
                result=result[1:]
            return result
        return repr(der(parse(expression)))
    def der_ln(expression):
        def parse(expression):
            return expression[3:].replace(')','')
        return f'{derivative(parse(expression))}/({parse(expression)})'
    
    def der_root(root,expr): #Переделать как степень
        return f'{derivative(expr)}/{root}*root({root},{expr}**{root-1})'
    if 'ln' not in expression and 'root' not in expression:
        return polynomial_derivative(expression)
    if expression[0]+expression[1]=='ln':
        return der_ln(expression)
    if expression[:4]=='root':
        return der_root(expression)
    e=split_expression(expression)
    l=[]
    for i in e:
        l.append(derivative(i))
    return l
print(derivative('ln(3x^2+x)-sin(x)-2x^2+x-1'))

def sol(expr):
    def get_coeffs(expression):
        expression += ' '  # Добавляем пробел в конец для корректной работы с последним символом
        result = []  # Список для сбора новой строки
        i = 0  # Индекс для обхода строки
        while i < len(expression):
            if expression[i] in num and (i + 1 < len(expression) and expression[i + 1] != 'x' and expression[i-1]!='^'):
                # Если символ — это число и за ним не идёт 'x'
                result.append(expression[i])
                result.append('x^0')  # Вставляем 'x^0'
            elif expression[i] == 'x' and (i + 1 < len(expression) and expression[i + 1] != '^'):
                # Если символ — это 'x', но за ним не идёт '^'
                result.append(expression[i])
                result.append('^1')  # Вставляем '^1'
            else:
                # Просто добавляем символ в результат
                result.append(expression[i])
            i += 1
        expression=''.join(result)
        pattern = r'[+-]?\d*x(?:\^\d+)?'
        terms = re.findall(pattern, expression)
        spl=[]
        for i in terms:
            spl.append(i.split('x'))
        for i, (x, y) in enumerate(spl):  
            z = y.replace('^', '')
            spl[i] = (x, z)
        return spl
    def sol(coeff):
        guess=coeff[-1][0]/coeff[0][0]
        answer=guess+derivative(expr)/expr #сделать версию производной где она будет возвращать функцию