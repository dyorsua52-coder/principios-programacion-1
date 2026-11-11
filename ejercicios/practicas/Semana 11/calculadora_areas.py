PI = 3.1416
OPCION_SALIR = 4

# Muestra el título del programa
def mostrar_encabezado():
    print("===================================")
    print("      CALCULADORA DE ÁREAS")
    print("===================================")

# Muestra las opciones del menú, una por línea
def mostrar_menu():
    print("1. Rectángulo")
    print("2. Triángulo equilatero")
    print("3. Círculo")
    print("4. Salir")

# Lee base y altura, calcula y muestra el área del rectángulo
# calcularAreaRectangulo
def calcular_area_rectangulo():
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    area = base * altura
    print("Área del rectángulo:", area)

# Lee base y altura, calcula y muestra el área del triángulo
def calcular_area_triangulo(base):
    altura = float(input("Altura: "))
    area = base * altura / 2
    return area

def calcular_perimetro_triangulo(lado): 
    perimetro = 3 * lado
    return perimetro


# Lee el radio, calcula y muestra el área del círculo (2 decimales)
def calcular_area_circulo():
    radio = float(input("Radio: "))
    area = PI * radio * radio
    print("Área del círculo:", round(area, 2))

# Función principal: muestra el encabezado y repite el menú hasta salir
def main():
    mostrar_encabezado()
    opcion = 0
    while opcion != OPCION_SALIR:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            calcular_area_rectangulo()
        elif opcion == 2:
            base = float(input("Base: "))
            area = calcular_area_triangulo(base)
            perimetro = calcular_perimetro_triangulo(base)
            print("Área del triángulo:", area, "y perimetro del triángulo:", perimetro)
        elif opcion == 3:
            calcular_area_circulo()
        elif opcion != OPCION_SALIR:
            print("Opción no válida.")
    print("Gracias por usar la calculadora.")

if __name__ == "__main__":
    main()