
import sympy as sp

#Definindo as variáveis
x = sp.symbols('x')

#Definindo a função g(x)
g_x = 2 * x + 1

#Definindo a função f(u) onde u = g(x)
u = sp.symbols('u')
f_u = u**2 + 3 * u

#Substituindo u por g(x) em f(u)    
f_g_x = f_u.subs(u, g_x)

#Calculando a derivada de f(g(x)) em relação a x
derivada = sp.diff(f_g_x,x)

#Exibindo o resultado
print(f"f'(g(x)) = {f_g_x}")
print(f"f'(g(x))' = {derivada}")

#Exercício 2
#Definindo as variáveis
t = sp.symbols('t')

#Definindo a função P(t)
P_t = 5 * t**2 + 3 * t + 2

P = sp.symbols('P')
T_P = 2*P**3 + 4*P

#Calculando a derivada de T(P) em relação a P


#Substituindo P por P(t) em T(P)
T_P_t = T_P.subs(P, P_t)
derivada = sp.diff(T_P_t,t)

#Exibindo o resultado
print(f"T(P(t)) = {T_P_t}")
print(f"T(P(t))' = {derivada}")
