#exp 6 2.2
import matplotlib.pyplot as plt
import numpy as np

def func(x):
    return x**2

def trapezoidal_rule(func, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = func(x)
    integral = h * (np.sum(y) - 0.5 * (y[0] + y[-1]))
    return integral

def simpsons_rule(func, a, b, n):
    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's rule")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = func(x)
    integral = h / 3 * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])
    return integral
a, b = 0, 2
true_value = 2.6666666666666665
print(f'True Integral Value: {true_value}')
n_values = [4, 8, 16, 32, 64]
for n in n_values:
    trapezoidal_result = trapezoidal_rule(func, a, b, n)
    simpsons_result = simpsons_rule(func, a, b, n)
    print(f'n={n}: Trapezoidal Result={trapezoidal_result:.4f}, Simpsons Result={simpsons_result:.4f}')
x_values = np.linspace(a, b, 100)
plt.plot(x_values, func(x_values), label='$x^2$ function')
plt.fill_between(x_values, func(x_values), alpha=0.2, label='Area under the curve')

plt.title('Numerical Integration Experiment')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
