import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

n = input('n:?')

x = sp.Symbol('x')

def fun_x(s):
    f = sp.sympify(s)
    f_func = lambda x: f.subs({'x':x})
    return f_func

# ************ iteraciones ************
#Pol = abs(x)
Pn = fun_x('0*x')
f= [Pn]
for i in range(n):
	aux = str(f[-1](x)) + '+(x**2-('+ str(f[-1](x))+')**2)/2.'
	Pn = fun_x(aux)
	f.append(Pn)

# ************   imprimir  ************
print '\n***** Polinomios en forma de iteracion *****\n'
for k in range(1,n+1):
	print f[k](x)

print '\n***** Polinomios en forma de base canonica *****\n'
for k in range(1,n+1):
	print sp.expand(f[k](x))	

# ************   graficar  ************
t = np.arange(-1,1,0.05)
g0 = sp.lambdify(x,abs(x),'numpy')
y = g0(t)
plt.plot(t,y,'r^')

color = plt.cm.rainbow(np.linspace(0,1,n))
for i,c in zip(range(1,len(f)),color):
	f0 = sp.lambdify(x,f[i](x),'numpy')
	y = f0(t)
	plt.plot(t,y,c=c)
plt.show()
