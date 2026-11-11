# Estudiante: Dylan Garos Quesada
# Problema 1: Emisiones asociadas al transporte

cantidad_estudiantes = int(input("Cantidad de estudiantes: "))
distancia = float(input("Distancia recorrida por cada estudiante (km): "))
factor_emision = float(input("Factor de emisión (kg CO2/km): "))

emisiones_totales = cantidad_estudiantes * distancia * factor_emision

print("\n--- Resultado ---")
print(f"Emisiones totales estimadas: {emisiones_totales:.2f} kg de CO2")