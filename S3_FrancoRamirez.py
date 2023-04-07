#IGNORE
#DIBUJO ENCONTRADO EN INTERNET https://es.stackoverflow.com/questions/351365/imprimir-un-rombo-con-asteriscos-de-ancho-n-con-n-impar
print("\n")

def dibujo_rombo(valor):
  result1 = [" " * (valor - i) + "*" * (i + i - 1) for i in range(1, valor + 1)]

  return "\n".join(result1 + list(reversed(result1[:-1])))

print(dibujo_rombo(5))

print("\n")

# EJERCICIO

totalProductos = 0
descSietePorc = 0
descDocePorc = 0
precioProductos =  int(input("Ingrese monto del producto(Cero para salir): "))

while (precioProductos != 0):
    totalProductos +=precioProductos
    precioProductos =  int(input("Ingrese monto del producto(Cero para salir): "))
    
print("\n\n")

print("La sumatoria de todos los precios ingresados (total de la venta sin descuentos): ", totalProductos)

if(totalProductos>=50000):
    descDocePorc = totalProductos * 12 / 100
    print("El monto de descuento logrado: ", descDocePorc)
    print("El monto a pagar (con los descuentos aplicados): ", totalProductos - descDocePorc)
else:
    descSietePorc = totalProductos * 7 / 100
    print("El monto de descuento logrado: ", descSietePorc)
    print("El monto a pagar (con los descuentos aplicados): ", totalProductos - descSietePorc)



print("\n")
