import sympy as sp 
import numpy as np
import matplotlib.pyplot as plt

x = sp.Symbol('x')
C = 10*x**2 - 4000*x + 5000 
 
C_prime = sp.diff(C, x)

critica1_point = sp.solve(C_prime, x) [0]

min_cost = C.subs(x, critica1_point)

C_func = sp.lambdify(x, C, 'numpy')

x_vals = np.linspace(-300,100,400)
C_vals = C_func(x_vals)

plt.figure(figsize=(10,6))
plt.plot(x_vals, C_vals, label='C(x) = 10x^2 + 4000x + 5000', color='blue')
plt.scatter([critica1_point], [min_cost], color ='red', zorder=5)
plt.text(critica1_point, min_cost,f'Min: ({critica1_point:.2f}, {min_cost:.2f})', horizontalalignment='right',
verticalalignment='top')
plt.axvline(x=critica1_point, color='red', linestyle='--')
plt.axhline(y=min_cost, color='red', linestyle='--')
plt.legend()
plt.grid(True)
plt.show()