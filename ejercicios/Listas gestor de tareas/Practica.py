# Gestor de tareas
tareas = []                                  # 1. Crear la lista vacía
opcion = 0
while opcion != 4:
    print("\n--- Gestor de tareas ---")
    print("1. Agregar una tarea")
    print("2. Completar una tarea")
    print("3. Mostrar las tareas pendientes")
    print("4. Salir")
    opcion = int(input("Seleccione una opción (1, 2, 3 o 4): "))
    if opcion == 1:
        tarea_nueva = input("Ingrese el nombre de la tarea: ")
        tareas.append(tarea_nueva)                    # 2. Agregue tarea_nueva al final de la lista
        print("Tarea agregada.")
    elif opcion == 2:
        if len(tareas) == 0:                                # 3. Condición: la lista está vacía
            print("No hay tareas pendientes.")
        else:
            numero = 1
            for tarea in tareas:                           # 4. Recorra la lista tareas
                print(numero, "-", tarea)
                numero = numero + 1
            numero_tarea = int(input("Ingrese el número de la tarea completada: "))
            if 1 <= numero_tarea <= len(tareas):                            # 5. Condición: el número está entre 1 y la cantidad de tareas
                completada = tareas.pop(numero_tarea - 1)               # 6. Elimine la tarea de la lista
                print("Tarea completada:", completada)
            else:
                print("Número de tarea no válido.")
    elif opcion == 3:
        if len(tareas) == 0:
            print("No hay tareas pendientes.")
        else:
            print("Tareas pendientes:", len(tareas))   # 7. Cantidad de tareas
            for tarea in tareas:
                print("-", tarea)
    elif opcion == 4:
        print("¡Lo esperamos pronto!")
    else:
        print("Opción no válida.")


        # 1. tareas = []
# Crea una lista vacía donde se guardarán las tareas pendientes.

# 2. tareas.append(tarea_nueva)
# Agrega la nueva tarea al final de la lista.

# 3. len(tareas) == 0
# Comprueba si la lista está vacía, es decir, si tiene 0 tareas.

# 4. for tarea in tareas:
# Recorre la lista para mostrar las tareas una por una.

# 5. 1 <= numero_tarea <= len(tareas)
# Comprueba que el número ingresado esté dentro del rango de tareas disponibles.

# 6. completada = tareas.pop(numero_tarea - 1)
# Elimina la tarea seleccionada de la lista y guarda su nombre en la variable completada.

# 7. len(tareas)
# Cuenta cuántas tareas hay actualmente en la lista.