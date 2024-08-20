#exp 3.1

from scipy.optimize import minimize
def objective_function(x):
    return x[0]**2 + x[1]**2
def constraint_equation(x):
    return x[0] + x[1] - 1
def optimize_with_constraints(initial_guess):
    constraints = {'type': 'eq', 'fun': constraint_equation}
    result = minimize(objective_function, initial_guess, constraints=constraints)
    return result

initial_guess = [0.5, 0.5]

result = optimize_with_constraints(initial_guess)

print("Optimal solution:", result.x)
print("Optimal value:", result.fun)
print("Lagrange multiplier (approx):", result.jac[0])
