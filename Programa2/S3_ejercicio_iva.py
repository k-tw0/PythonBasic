"""
    Dada la venta de una seria INDETERMINADAD de productos que
    estan sin IVA.
    Se desea conocer:
    *** el precio total sin IVA
    *** el monto del IVA
    *** el precio total a pagar con IVA incluido
    Considerar el precio CERO para el termino de ingreso de precios

"""

#   EJERCICIO 1 WHILE

"""

totalSinIVA = 0 # Inicializacion
precioSinIVA =  int(input("Ingrese precio sin IVA (Cero para salir): "))

while (precioSinIVA != 0):
    totalSinIVA = totalSinIVA + precioSinIVA # ACUMULADOR
    precioSinIVA =  int(input("Ingrese precio sin IVA (Cero para salir): "))

totalIVA = totalSinIVA * 19 / 100 # EL PRECIO MULTIPLICADO x19 Y DIVIDIDO POR 100
totalConIVA = totalSinIVA + totalIVA # CALCULA EL TOTAL

print("Total sin IVA: ", totalSinIVA)
print("Total IVA: ", totalIVA)
print("Total con IVA: ", totalConIVA)

"""

#   EJERCICIO 2 for

totalSinIVA = 0
cantidad_prod = int(input("Cuantos productos pasara?: "))

for i in range(1, cantidad_prod + 1, 1):
    precioSinIVA = int(input("Ingrese precio sin IVA: "))
    totalSinIVA =  totalSinIVA + precioSinIVA # acumulador

totalIVA = totalSinIVA * 19 / 100 # EL PRECIO MULTIPLICADO x19 Y DIVIDIDO POR 100
totalConIVA = totalSinIVA + totalIVA # CALCULA EL TOTAL

print("Total sin IVA: ", totalSinIVA)
print("Total IVA: ", totalIVA)
print("Total con IVA: ", totalConIVA)
