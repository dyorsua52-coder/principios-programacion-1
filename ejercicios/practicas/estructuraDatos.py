# Una estructura de datos es una forma de organizar datos en memoria para poder operarlos eficientemente (buscar, insertar, borrar, recorrer…).

"""
Estructura de datos (concepto)	    Python	                    Java	                C++	                        JavaScript	        
Array / arreglo	                    list (dynamic array)	    ArrayList / arrays	    std::vector	                Array	        
                                    tuple                       -                       std::tuple / std::pair      -
Lista enlazada	                    -	                        LinkedList	            std::list	                -	                
Pila (stack)	                    list (con .append/.pop)	    Deque/Stack	            std::stack	                Array	            
Cola (queue)	                    collections.deque	        Queue	                std::queue	                -                   
Tabla hash (mapa)	                dict	                    HashMap	                std::unordered_map	        Map	
Conjunto (set)	                    set / frozenset	            HashSet	                std::unordered_set	        Set	
Árbol	                            -                           TreeMap	                std::map	                -	
"""

ejemploLista = ["Dato 1", 2, "Dato índice 2"]
ejemploLista.append([12.5, -86.3])
ejemploLista.pop(1)
ejemploLista[1] = "Dato índice 1"
print("Lista:", ejemploLista)
print(type(ejemploLista))

# Tupla: Datos inmutables
ejemploTupla = ("amarillo", 9, True, 12.3, "a") 
print("Tupla:", ejemploTupla)
print("Tupla posición 1:", ejemploTupla[1])

PROVINCIAS = ["San José", "Cartago", "Puntarenas", "Limón", "Guanacaste", "Heredia", "Alajuela"]
provinciasTupla = ("San José", "Cartago", "Puntarenas", "Limón", "Guanacaste", "Heredia", "Alajuela")


# Conjuntos 
ejemploConjuntos = {1, 2, 3, 4}
print("Conjunto:", ejemploConjuntos)

ejemploConjuntos.add(5)
ejemploConjuntos.add(2)
ejemploConjuntos.add("azul")
print("Conjunto actualizado:", ejemploConjuntos)