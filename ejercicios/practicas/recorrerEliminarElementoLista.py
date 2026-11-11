# Eliminar un elemento de la lista por índice 
animales = ["Caballo", "Vaca", "Perro", "Gato"]

# Mostrar los elementos con numeración desde 1
for indice, nombre in enumerate(animales):
    print(indice + 1, "-", nombre)

# Solicitar el elemento que desea eliminar
opcion = int(input("Ingrese el número del elemento que desea eliminar: "))

# Eliminar el elemento seleccionado
if opcion >= 1 and opcion <= len(animales):
    animales.pop(opcion - 1)

# Mostrar la lista actualizada
print("Lista actualizada:")

for indice, nombre in enumerate(animales, start=1):
    print(indice, "-", nombre)