compra = float(input("Monto de la compra: "))
descuento = 0

if compra >= 100000:
    descuento = compra * 0.15
elif compra >= 60000:
    descuento = compra * 0.10
elif compra >= 30000:
    descuento = compra * 0.05

total = compra - descuento

print("===========Descuento obtenido===========")
print(descuento)

print("===========Total a pagar===========")
print(total)

# entrada: 20.000
# salida: 
# descuento: 0.0
# total: 20000.0

# entrada: 29.999
# salida: 
# descuento: 0
# total: 29999.0

# entrada: 30.000
# salida:
# descuento: 1500.0
# total: 28500.0

# entrada: 45.000
# salida:
# descuento: 2250.0
# total: 42750.0

# entrada: 60.000
# salida:
# descuento: 6000.0
# total: 54000.0

# entrada: 80.000
# salida:
# descuento: 8000.0
# total: 72000.0

# entrada: 100.000
# salida:
# descuento: 15000.0
# total: 85000.0

# entrada: 150.000
# salida:
# descuento: 22500.0
# total: 127500.0



#Codigo original con errores

#compra = float( input( "Monto de la compra: "))
#descuento = 0
#if compra > 30000:
#descuento = compra * 0.05
#elif compra > 60000:
#descuento = compra * 0.10
#elif compra > 100000:
#descuento = compra * 0.15
#total = compra - descuento
#print( "Descuento:", descuento)
#print( "Total:", total)

#₡20 000
#Monto de la compra: 20000
#Descuento: 0
#Total: 20000.0

#₡30 000
#Monto de la compra: 30000
#Descuento: 0
#Total: 30000.0

#₡45 000
#Monto de la compra: 45000 
#Descuento: 2250.0
#Total: 42750.0

#₡60 000
#Monto de la compra: 60000
#Descuento: 3000.0
#Total: 57000.0

#₡80 000
#Monto de la compra: 80000      
#Descuento: 4000.0
#Total: 76000.0

#₡100 000
#Monto de la compra: 100000
#Descuento: 5000.0
#Total: 95000.0

#₡120 000
#Monto de la compra: 120000
#Descuento: 6000.0
#Total: 114000.0

#Todos los montos dan siempre el mismo descuento, ya que la condición de los if y elif no están bien planteadas.
#Por ende todas cumplen la primera condicion de 30000, y nunca se llega a evaluar las demás condiciones. 