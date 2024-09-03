import numpy as np
import sympy as smp
import matplotlib.pyplot as plt

# Define the variables



#Interval
min = 0
max = 24
n = 8

#Tamanho do intervalo
dx = (max - min)/n

#Transformando função
x = smp.symbols('x')
f = 2*x**2 
f_x = smp.lambdify(x, f)

#Criar a sequência de pontos para o eixo X 
eixo_x = np.arange(min, max, dx)

#Criar a sequência de pontos para o eixo Y
eixo_y = [f_x(i) for i in eixo_x]

#Criar o gráfico
plt.bar(x = eixo_x, height = eixo_y, width = 2)
plt.plot(eixo_x, eixo_y, color = 'k')
plt.show()
