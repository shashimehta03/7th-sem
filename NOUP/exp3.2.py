#exp3.2
from scipy.optimize import minimize
def objective_function(x):
    return x[0]**2 + x[1]**2
def equality_constraint(x):
    return x[0] + x[1] - 1

def inequality_constraint(x):
    return x[0] - x[1]
initial_guess = [0.5, 0.5]
constraints = [
    {'type': 'eq', 'fun': equality_constraint},
    {'type': 'ineq', 'fun': inequality_constraint}
]
result = minimize(objective_function, initial_guess, constraints=constraints)
print("Optimal solution:", result.x)
print("Optimal value:", result.fun)
print("Success:", result.success)
print("Message:", result.message)
