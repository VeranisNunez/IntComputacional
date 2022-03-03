"""
Haga un programa en Python que permita ingresar el dinero invertido por
tres personas para formar una empresa. Cada una de ellas invierte una
cantidad distinta. Imprimir el porcentaje que cada quien invierte con respecto
al total de la inversión.
"""

inversion1 = float(input('Ingrese cantidad de inversion 1: '))
inversion2 = float(input('Ingrese cantidad de inversion 2: '))
inversion3 = float(input('Ingrese cantidad de inversion 3: '))
total = (inversion1 + inversion2 + inversion3)

valor1 = round((inversion1/total)*100)
valor2 = round((inversion2/total)*100)
valor3 = round((inversion3/total)*100)
print(f'Persona 1 : {valor1:,}% \nPersona 2 : {valor2:,}%  \nPersona 3 : {valor3:,}% ')