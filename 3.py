"""
Un vendedor recibe un sueldo base más un 15% extra por comisión de sus
ventas efectuadas en el mes. El vendedor desea saber cuanto dinero en
total obtendrá por las ventas que realiza en el mes. Desarrolle un programa
en Python que permita mostrar el valor ganado por comisión y el valor total
a pagar al vendedor.
"""

sueldo = float(input('Ingrese el sueldo del vendedor : '))
ventas = float(input('Ingrese valor de ventas efectuadas en el mes : '))
comision = ventas + (ventas*0.15)

print(f'Valor de comisión: {comision:,} \nValor total: {sueldo+comision:,}')