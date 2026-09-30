# Solicitar los datos del estudiante
promedio = float(input("Ingrese su promedio académico: "))
asistencia = float(input("Ingrese su porcentaje de asistencia: "))
programa_apoyo = input("¿Pertenece a un programa de apoyo? (si/no): ")

# Primera condición:
# El estudiante debe tener un promedio de 80 o más
# y una asistencia de 85% o más.
condicion_academica = promedio >= 80 and asistencia >= 85

# Segunda condición:
# El estudiante debe pertenecer al programa de apoyo
# y tener una asistencia de 75% o más.
condicion_apoyo = programa_apoyo == "si" and asistencia >= 75

# El estudiante obtiene la beca si cumple
# la primera condición o la segunda condición.
if condicion_academica or condicion_apoyo:
    print("Obtiene la beca.")
else:
    print("No obtiene la beca.")