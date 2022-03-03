"""
Un alumno desea saber cuál será su calificación final en la materia de
fundamentos de programación. Dicha calificación se compone de los
siguientes porcentajes: 50% del promedio de sus tres talleres, 30% de la
calificación de un examen en clase y 20% de la calificación de un proyecto
final.
"""

taller1 = float(input('Nota de taller 1: '))
taller2 = float(input('Nota de taller 2: '))
taller3 = float(input('Nota de taller 3: '))
examen = float(input('Nota de examen: '))
proyecto = float(input('Nota de proyecto: '))

talleres = ((taller1+taller2+taller3)*0.5)/3
final = talleres + (examen*0.3) + (proyecto*0.2)

print(f'La calificaión final del alumno: {final}')