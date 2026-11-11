# ==========================================================
#                    APUNTES DE PYTHON
# ==========================================================


# ==========================================================
# IF
# ==========================================================
# Sirve para tomar una decisión.
# Significa: "SI se cumple esta condición, haz esto."

# Ejemplo:
# if edad >= 18:
#     print("Es mayor de edad")


# ==========================================================
# ELIF
# ==========================================================
# Significa: "SI NO, PERO SI..."
# Sirve para comprobar otra condición si el if anterior
# no se cumplió.

# Ejemplo:
# if edad >= 18:
#     print("Adulto")
# elif edad >= 12:
#     print("Adolescente")


# ==========================================================
# ELSE
# ==========================================================
# Significa: "SI NO".
# Se ejecuta cuando ninguna de las condiciones anteriores
# se cumple.

# Ejemplo:
# if edad >= 18:
#     print("Adulto")
# else:
#     print("Menor de edad")


# ==========================================================
# WHILE
# ==========================================================
# Sirve para repetir algo MIENTRAS una condición sea verdadera.

# Ejemplo:
# while edad < 18:
#     print("Todavía es menor")


# También se puede utilizar para validar respuestas.
#
# Ejemplo:
# while respuesta not in ["si", "sí", "no"]:
#     print("Respuesta inválida")
#     respuesta = input("Escriba si o no: ")


# ==========================================================
# AND
# ==========================================================
# Significa "Y".
# TODAS las condiciones deben cumplirse para que sea True.

# Ejemplo:
# if edad >= 18 and matriculado == "si":
#     print("Puede acceder")


# ==========================================================
# OR
# ==========================================================
# Significa "O".
# Solo UNA de las condiciones necesita cumplirse.

# Ejemplo:
# if edad >= 18 or tiene_permiso == "si":
#     print("Puede acceder")


# ==========================================================
# NOT
# ==========================================================
# Significa "NO" o lo contrario.
# Cambia True por False y False por True.

# Ejemplo:
# if not activo:
#     print("La cuenta está inactiva")


# ==========================================================
# IN
# ==========================================================
# Significa "ESTÁ DENTRO DE".
# Sirve para comprobar si un valor está dentro de una lista.

# Ejemplo:
# if respuesta in ["si", "sí", "no"]:
#     print("Respuesta válida")


# ==========================================================
# NOT IN
# ==========================================================
# Significa "NO ESTÁ DENTRO DE".

# Ejemplo:
# if respuesta not in ["si", "sí", "no"]:
#     print("Respuesta inválida")


# ==========================================================
# INPUT()
# ==========================================================
# Sirve para pedir información al usuario.
# Lo que escribe el usuario normalmente se guarda como TEXTO.

# Ejemplo:
# nombre = input("Ingrese su nombre: ")


# ==========================================================
# INT()
# ==========================================================
# Convierte un valor en un NÚMERO ENTERO.
#
# Se utiliza mucho junto con input() cuando queremos
# que el usuario escriba un número.

# Ejemplo:
# edad = int(input("Ingrese su edad: "))


# ==========================================================
# FLOAT()
# ==========================================================
# Convierte un valor en un número que puede tener DECIMALES.

# Ejemplo:
# precio = float(input("Ingrese el precio: "))


# ==========================================================
# STR()
# ==========================================================
# Convierte un valor en TEXTO.

# Ejemplo:
# edad = 19
# texto = str(edad)


# ==========================================================
# PRINT()
# ==========================================================
# Sirve para mostrar información en la pantalla.

# Ejemplo:
# print("Hola")
# print(edad)


# ==========================================================
# .LOWER()
# ==========================================================
# Convierte un texto a MINÚSCULAS.

# Ejemplo:
# respuesta = "SI"
# respuesta.lower()
#
# Resultado:
# "si"


# ==========================================================
# .UPPER()
# ==========================================================
# Convierte un texto a MAYÚSCULAS.

# Ejemplo:
# nombre = "dylan"
# nombre.upper()
#
# Resultado:
# "DYLAN"


# ==========================================================
# .STRIP()
# ==========================================================
# Elimina espacios al principio y al final de un texto.

# Ejemplo:
# respuesta = "   si   "
# respuesta.strip()
#
# Resultado:
# "si"


# ==========================================================
# ==
# ==========================================================
# Significa "ES IGUAL A".
# Se utiliza para COMPARAR valores.

# Ejemplo:
# if edad == 18:
#     print("Tiene exactamente 18 años")


# ==========================================================
# =
# ==========================================================
# Sirve para ASIGNAR o GUARDAR un valor en una variable.
#
# IMPORTANTE:
# "=" NO significa "es igual a" cuando estamos comparando.

# Ejemplo:
# edad = 18
#
# Esto significa:
# "Guardar 18 dentro de la variable edad."


# ==========================================================
# !=
# ==========================================================
# Significa "ES DIFERENTE DE".

# Ejemplo:
# if edad != 18:
#     print("No tiene 18 años")


# ==========================================================
# >
# ==========================================================
# Significa "MAYOR QUE".

# Ejemplo:
# if edad > 18:
#     print("Tiene más de 18 años")


# ==========================================================
# <
# ==========================================================
# Significa "MENOR QUE".

# Ejemplo:
# if edad < 18:
#     print("Tiene menos de 18 años")


# ==========================================================
# >=
# ==========================================================
# Significa "MAYOR O IGUAL QUE".

# Ejemplo:
# if edad >= 18:
#     print("Tiene 18 años o más")


# ==========================================================
# <=
# ==========================================================
# Significa "MENOR O IGUAL QUE".

# Ejemplo:
# if edad <= 18:
#     print("Tiene 18 años o menos")


# ==========================================================
# LISTAS [ ]
# ==========================================================
# Sirven para guardar VARIOS valores dentro de una sola variable.

# Ejemplo:
# opciones = ["si", "sí", "no"]


# ==========================================================
# TRUE Y FALSE
# ==========================================================
# Son valores booleanos.
#
# True  = Verdadero
# False = Falso

# Ejemplo:
# edad = 20
#
# edad >= 18
#
# Resultado:
# True


# ==========================================================
# VARIABLES
# ==========================================================
# Sirven para guardar información.
# Puedes imaginar una variable como una "caja" que contiene
# un valor.

# Ejemplo:
# edad = 19
# nombre = "Dylan"
# matriculado = "si"


# ==========================================================
# RESUMEN RÁPIDO
# ==========================================================
#
# if       = SI
# elif     = SI NO, PERO SI
# else     = SI NO
# while    = REPETIR MIENTRAS
#
# and      = Y
# or       = O
# not      = NO / contrario
# in       = ESTÁ DENTRO DE
# not in   = NO ESTÁ DENTRO DE
#
# input()  = PEDIR DATOS
# int()    = CONVERTIR A ENTERO
# float()  = CONVERTIR A DECIMAL
# str()    = CONVERTIR A TEXTO
# print()  = MOSTRAR EN PANTALLA
#
# .lower() = MINÚSCULAS
# .upper() = MAYÚSCULAS
# .strip() = QUITAR ESPACIOS
#
# ==       = IGUAL A
# !=       = DIFERENTE DE
# >        = MAYOR QUE
# <        = MENOR QUE
# >=       = MAYOR O IGUAL
# <=       = MENOR O IGUAL
#
# =        = GUARDAR / ASIGNAR UN VALOR
#
# True     = VERDADERO
# False    = FALSO
#
# ==========================================================