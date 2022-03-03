"""
Una Institución educativa ha recibido una donación especial que será
repartida entre las carreras de Telecomunicaciones, Sistemas,
Administración y Contabilidad de la siguiente forma:
a. Telecomunicaciones 10% del valor dado a sistemas
b. Sistemas: 25% del valor dado a Administración
c. Administración: 35% del valor de la donación
d. Contabilidad: lo que resta de la donación
"""

donacion = float(input('Ingrese el valor de donación: '))
telecomunicaciones = donacion*0.1
sistemas = donacion*0.25
administración = donacion*0.35
contabilidad = donacion - (telecomunicaciones + sistemas + administración)

print(f'Telecomunicaciones : ${telecomunicaciones:,} \nSistemas: ${sistemas:,}  \nAdministración: ${administración:,} \nContabilidad: ${contabilidad:,}')