promedio = float(input("Ingrese su promedio académico: "))
asistencia = float(input("Ingrese su porcentaje de asistencia: "))
programa_apoyo = input("¿Pertenece a un programa de apoyo? (si/no): ")

# Verificar si el estudiante cumple alguna de las condiciones para obtener la beca
if (promedio >= 80 and asistencia >= 85) or (programa_apoyo == "si" and asistencia >= 75):
    print("Obtiene la beca.")
else:
    print("No obtiene la beca.")