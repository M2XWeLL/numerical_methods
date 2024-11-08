import cmath
from default import *
from trigonometry import *

def solve_cubic(a, b, c, d):
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a cubic equation.")

    # Приводим уравнение к виду t^3 + pt + q = 0
    p = (3 * a * c - b**2) / (3 * a**2)
    q = (2 * b**3 - 9 * a * b * c + 27 * a**2 * d) / (27 * a**3)

    # Вычисляем дискриминант
    delta = (q / 2)**2 + (p / 3)**3

    if delta > 0:
        # Один действительный корень и два комплексных корня
        u = (-q / 2 + root(2,delta))**(1/3)
        v = (-q / 2 - root(2,delta))**(1/3)
        t1 = u + v
        t2 = -(u + v) / 2 + root(2,3) * (u - v) / 2 * 1j
        t3 = -(u + v) / 2 - root(2,3) * (u - v) / 2 * 1j
    elif delta == 0:
        # Три действительных корня, из которых два или все три могут быть равными
        if q == 0:
            t1 = t2 = t3 = 0
        else:
            u = (-q / 2)**(1/3)
            t1 = 2 * u
            t2 = t3 = -u
    else:
        # Три действительных корня
        r = root(2,-(p / 3)**3)
        theta = cmath.acos(-q / (2 * r))
        t1 = 2 * r**(1/3) * Cos(theta / 3)
        t2 = 2 * r**(1/3) * Cos((theta + 2 * pi) / 3)
        t3 = 2 * r**(1/3) * Cos((theta + 4 * pi) / 3)

    # Возвращаемся к переменной x
    x1 = t1 - b / (3 * a)
    x2 = t2 - b / (3 * a)
    x3 = t3 - b / (3 * a)

    return (x1, x2, x3)
def solve_quartic(a, b, c, d, e):
    # Приводим к каноническому виду: y^4 + py^2 + qy + r = 0
    p = (8*a*c - 3*b**2) / (8*a**2)
    q = (b**3 - 4*a*b*c + 8*a**2*d) / (8*a**3)
    r = (-3*b**4 + 256*a**3*e - 64*a**2*b*d + 16*a*b**2*c) / (256*a**4)

    # Решаем вспомогательное кубическое уравнение
    cubic_a = 1
    cubic_b = 2*p
    cubic_c = p**2 - 4*r
    cubic_d = -q**2
    roots = solve_cubic(cubic_a, cubic_b, cubic_c, cubic_d)

    # Выбираем один из корней кубического уравнения
    y = max(roots, key=lambda x: x.real).real

    # Вычисляем квадратные корни
    R = cmath.sqrt(y**2 - r)
    D = cmath.sqrt(2*y - p + 2*cmath.sqrt(y**2 - r))
    E = cmath.sqrt(2*y - p - 2*cmath.sqrt(y**2 - r))

    x1 = (-b/(4*a)) + (R+D)/2
    x2 = (-b/(4*a)) + (R-D)/2
    x3 = (-b/(4*a)) - (R+E)/2
    x4 = (-b/(4*a)) - (R-E)/2

    return (x1, x2, x3, x4)