colores = ["rojo", "blanco", "amarillo", "azul", "verde"]

videojugos_venta = ["Zelda Breath of the Wild", "Smash Bros", "Mario Kart", "Minecraft"]

# Recorrer uns lista con un ciclo for
"""
colores = [
    "rojo", 
    "blanco", 
    "amarillo", 
    "azul", 
    "verde"
]
"""
    # nombreSignificativoElementoLista
for color in colores: 
    print("Color:", color)

for elemento in videojugos_venta:
    print("Nombre del videojuego:", elemento)

apellidos = ["ANGULO", "CASTILLO", "CABAS", "FUENTES", "HERNANDEZ"]
"""
apellidos = ["ANGULO", "CASTILLO", "CABAS", "FUENTES", "HERNANDEZ"]
item = ANGULO
    Apellido: ANGULO
item = CASTILLO
    Apellido: CASTILLO 
item = CABAS
    Apellido: CABAS
item = FUENTES
    Apellido: FUENTES
item = HERNANDEZ
    Apellido: HERNANDEZ
"""
for item in apellidos: 
    print("Apellido:", item)


tazaDeMedida = [1.5, 2.5, 3.5, 4.5, 5.5]
"""
dobleTaza = [] 

elemento = 1.5
    doble = 2 * 1.5 = 3.0
    dobleTaza.append(3.0) -> dobleTaza = [3.0]

elemento = 2.5 
    doble = 2 * 2.5 = 5.0
    dobleTaza.append(5.0) -> dobleTaza = [3.0, 5.0]

elemento = 3.5
    doble = 2 * 3.5 = 7.0
    dobleTaza.append(7.0) -> dobleTaza = [3.0, 5.0, 7.0]

elemento = 4.5
    doble = 2 * 4.5 = 9.0
    dobleTaza.append(9.0) -> dobleTaza = [3.0, 5.0, 7.0, 9.0]

elemento = 5.5 
    doble = 2 * 5.5 = 11.0
    dobleTaza.append(11.0) -> dobleTaza = [3.0, 5.0, 7.0, 9.0, 11.0]

Lista de dobles: [3.0, 5.0, 7.0, 9.0, 11.0]
"""
dobleTaza = []
for elemento in tazaDeMedida:
    print("elemento = ", elemento)
    doble = 2 * elemento
    print("     doble = 2 *", elemento, "=", doble)
    dobleTaza.append(doble)
    print("     dobleTaza.append(", doble, ") -> dobleTaza =", dobleTaza, "\n")

print("Lista de dobles:", dobleTaza)

# Llenar una lista con 4 datos que ingresa el usuario 
notas = []
for i in range(4):
    # nota = float(input("Ingrese una nota: "))
    # notas.append(nota)
    notas.append(float(input("Ingrese una nota: ")))

print("Lista notas:", notas)

# Llenar una lista hasta que el usuario quiera salir
nombres = []
while True: 
    nombres.append(input("Ingrese un nombre: "))

    continuar = input("Ingrese 's' para salir o cualquier tecla para continuar: ")
    if continuar == "s":
        break # Termina el ciclo
print("Lista nombres:", nombres)


"""
colores = ["rojo", "blanco", "amarillo", "azul", "verde"]
              0       1           2         3        4  
"""
colores = ["rojo", "blanco", "amarillo", "azul", "verde"] 
print("----- Mostrar el índice de cada elemento en la lista y el elemento con while -----")
i = 0
while i < len(colores):
    print("Índice:", i, "- Nombre:", colores[i])
    i += 1

"""
enumerate(colores)

enumerate() permite iterar sobre un iterable, generando índices junto con los elementos

colores = ["rojo", "blanco", "amarillo", "azul", "verde"]
enumerate de colores:  
    -  0     "rojo", 
    -  1     "blanco", 
    -  2     "amarillo", 
    -  3     "azul", 
    -  4     "verde"
"""
print("----- Mostrar el índice de cada elemento en la lista y el elemento con for -----")
for indice, nombreColor in enumerate(colores):
    print("Índice:", indice,  "- Nombre:", nombreColor)