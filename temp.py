import numpy as np

def integrand(x):
    # Compute the function values
    values = np.sqrt(x**2 + np.sin(x))
    # Replace nan values with 0 or another small positive number
    values = np.where(np.isnan(values), 0, values)
    return values

def trapezoidal_rule(a, b, func, n=1000000):
    x = np.linspace(a, b, n+1)
    y = func(x)
    dx = (b - a) / n
    integral = (y[0] + y[-1]) / 2.0 + np.sum(y[1:-1])
    return integral * dx

a, b = -5, 5
result = trapezoidal_rule(a, b, integrand)
print(f"The numerical approximation of the integral is {result:.10f}")