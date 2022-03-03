"""
Dada la cantidad de alumnos de Redes, contabilidad y diseño determine el
porcentaje de alumnos de cada uno de los cursos.
"""

redes = int(input('Cantidad de alumnos de redes: '))
contabilidad = int(input('Cantidad de alumnos de contabilidad: '))
diseño = int(input('Cantidad de alumnos de diseño: '))

total = redes+contabilidad+diseño
p_redes = round((redes/total)*100)
p_contabilidad = round((contabilidad/total)*100)
p_diseño = round((diseño/total)*100)

print(f'Porcentaje de redes: {p_redes}% \nPorcentaje de contabilidad: {p_contabilidad}% \nPorcentaje de diseño: {p_diseño}%')