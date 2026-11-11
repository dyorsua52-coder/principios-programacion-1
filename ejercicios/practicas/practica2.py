# ==========================================
# VARIABLES
# ==========================================

# Pedir la edad
edad = int(input("Ingrese su edad: "))


# ==========================================
# VALIDAR SI / NO
# ==========================================

# Preguntar si está matriculado
matriculado = input("¿Está matriculado? (si/no): ").lower().strip()

while matriculado not in ["si", "sí", "no"]:
    print("Respuesta inválida. Escriba solamente 'si' o 'no'.")
    matriculado = input("¿Está matriculado? (si/no): ").lower().strip()


# Preguntar si tiene cuenta activa
cuenta_activa = input("¿Tiene cuenta activa? (si/no): ").lower().strip()

while cuenta_activa not in ["si", "sí", "no"]:
    print("Respuesta inválida. Escriba solamente 'si' o 'no'.")
    cuenta_activa = input("¿Tiene cuenta activa? (si/no): ").lower().strip()


# Preguntar si el servicio está pagado
servicio_pagado = input("¿Ha pagado el servicio? (si/no): ").lower().strip()

while servicio_pagado not in ["si", "sí", "no"]:
    print("Respuesta inválida. Escriba solamente 'si' o 'no'.")
    servicio_pagado = input("¿Ha pagado el servicio? (si/no): ").lower().strip()


# ==========================================
# CONDICIÓN
# ==========================================

if edad >= 18 and matriculado in ["si", "sí"] and cuenta_activa in ["si", "sí"] and servicio_pagado in ["si", "sí"]:
    print("Puede acceder al sistema.")
else:
    print("No puede acceder al sistema.")