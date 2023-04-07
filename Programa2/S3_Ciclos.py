#EJERCICIO 1

"""  
Conteo manual

print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)
print("Conteo finalizado")


"""

#EJERCICIO 2 WHILE

"""
Si tuvieramos que Ejecutar 5.000 peticiones print,
no conviene hacerlo de manera manual.

Para esto sirven los bucles o los ciclos,
Ciclo while(mientras), repeticiones.

cuenta = 1
while (cuenta <= 10): #Mientras cuenta, sea menor o igual a 10
    print(cuenta)# Mensaje
    cuenta = cuenta + 1 # Control del ciclo infinito.
print("Conteo finalizado")

"""

#EJERCICIO 3 WHILE

"""
Con el ciclo while se necesita manejar la finalizacion del ciclo,
con la variable cuenta.

Con el ciclo for tiene su propio metodo para salir,
de la repeticion.

desde = 1; hasta = 11; incremento = 1; 
for i in range(desde, hasta, incremento): # Para mi rango(1, 11, 1)
    print(i)# Mostrar rango
print("Conteo finalizado")

"""

#EJERCICIO 4 WHILE

"""
#Ciclo while de peticion n veces por consola
cantidad_veces = int(input("Hasta que numero desea contar?: "))
cuenta = 1
while (cuenta <= cantidad_veces):
    print(cuenta)
    cuenta = cuenta + 1 
print("Conteo finalizado")

"""

#EJERCICIO 5 FOR

"""

#Ciclo for de peticion n veces por consola
cantidad_veces = int(input("Hasta que numero desea contar?: "))
for i in range(1,cantidad_veces + 1, 1): # Para mi rango(1, 11, 1)
    print(i)# Mostrar rango
print("Conteo finalizado")

"""

    #   El ciclo while esta pensado para hacer repeticiones en una cantidad indeterminada de veces
    #   EL ciclo for esta pensado para hacer repeticiones en una cantidad determinada de veces