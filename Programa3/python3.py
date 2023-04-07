#SEMANAS DEL Año = 52
#CALCULAR CUANTAS AGUAS PARA ANIOS DE VIDA
totalSinIVA = 0
cantidad_prod = int(input("Cuantas botellas pasara: "))

for i in range(1, 2, 1):
    precio= int(input("Ingrese precio: "))
    total = cantidad_prod * precio # CALCULA EL TOTAL
    print("El costo total para las botellas de agua:$ ", total)
