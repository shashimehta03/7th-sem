#exp 2.3
import matplotlib.pyplot as plt
import numpy as np
def func(x):
    return x**2
def true_derivative(x):
    return 2 * x
def forward_difference(func, x, h):
    return (func(x + h) - func(x)) / h
x_value = 2.0
h_values = [0.1, 0.01, 0.001]
true_derivative_value = true_derivative(x_value)
print(f'True Derivative Value: {true_derivative_value}')

for h in h_values:
    numerical_derivative = forward_difference(func, x_value, h)
    print(f'h={h}: Numerical Derivative={numerical_derivative:.4f}')

x_values = np.linspace(0, 4, 100)

plt.plot(x_values, func(x_values), label='$x^2$ function')
plt.scatter(x_value, func(x_value), color='red', label='Point of Interest')

for h in h_values:
    tangent_line = true_derivative_value * (x_values - x_value) + func(x_value)
    plt.plot(x_values, tangent_line, linestyle='--', label=f'Tangent (h={h})')


plt.title('Numerical Differentiation Experiment')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
