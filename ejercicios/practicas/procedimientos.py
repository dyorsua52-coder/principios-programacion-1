KM_A_MILLAS = 0.621371
OPCION_SALIR = 3

# --- Convertir temperatura ---
def convertir_temperatura():    
    celsius = float(input("Grados Celsius: "))
    fahrenheit = celsius * 9 / 5 + 32
    print(celsius, "°C equivalen a", fahrenheit, "°F")

# --- Convertir distancia ---
def convertir_distancia():
    kilometros = float(input("Kilómetros: "))
    millas = kilometros * KM_A_MILLAS
    print(kilometros, "km equivalen a", round(millas, 2), "millas")

# --- Menú ---
def mostrar_menu():        
    print()
    print("1. Celsius a Fahrenheit")
    print("2. Kilómetros a millas")
    print("3. Salir")

# --- Encabezado ---
def mostrar_encabezado(nombre_usuario):
    print("===================================")
    print("      Bienvenido(a)", nombre_usuario)
    print("      CONVERSOR DE UNIDADES")
    print("===================================")

# --- Despedida ---
def mostrar_despedida(nombre_usuario):
    # Ejercicio: Modificar mostrar_despedidda para que muestre el nombre del usuario "Gracias nombre_usuario por usar el conversor"
    print("Gracias", nombre_usuario, "por usar el conversor.")

# --- Función principal ---
def main():
    nombre_usuario = input("Ingrese su nombre: ")
    mostrar_encabezado(nombre_usuario)
    opcion = 0
    while opcion != OPCION_SALIR:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            convertir_temperatura()

        elif opcion == 2:
            convertir_distancia()
            
        elif opcion != OPCION_SALIR:
            print("Opción no válida.")

    mostrar_despedida(nombre_usuario)


# Si este archivo se está ejecutando directamente, haga lo siguiente: 
if __name__ == "__main__":
    main()