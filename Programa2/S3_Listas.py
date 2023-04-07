""" 
    Listas. Variable multiposicion y con indice.
    ***Acciones:
        append() agregar
        pop() eliminar
        lista[position] leer/asignar
        len(lista)  longitud o cantidad de posiciones
"""

#   EJERCICIO 1 Calcular el promedio de 3 notas (sin usar listas)

""" 
nota1 = 6.5
nota2 = 4.8
nota3 = 5.8
promedio = (nota1 + nota2 + nota3) / 3
print("El promedio es: ", promedio)

"""

#   EJERCICIO 2 Calcular el promedio de 3 notas(utilizando listas)

""" 
notas = [6.5, 4.8, 5.8]
promedio = (notas[0] + notas[1] + notas[2]) / len(notas)
print(promedio)

"""

#   EJERCICIO 3 calcular promedio de notas ingresadas por el usuario
#   Sin usar listas, Terminar cuando se ingrese una nota cero

""" 
sumatoria_notas = 0 # Acumulador
cantidad_notas = 0 # Contador
nota = float(input("Ingrese una nota (CERO para salir): "))

while (nota > 0):
    sumatoria_notas = sumatoria_notas + nota # Acumalacion
    cantidad_notas = cantidad_notas + 1 # Conteo
    nota = float(input("Ingrese una nota (CERO para salir): "))
if(cantidad_notas > 0):
    promedio = sumatoria_notas / cantidad_notas
    print("El promedio es: ", promedio)
""" 

#   EJERCICIO 4 calcular promedio de notas ingresadas por el usuario
#   utilizando listas, Terminar cuando se ingrese una nota cero

"""
def sumar_notas(listado):
    suma = 0 # Acumulador
    for nota in listado:
        suma = suma + nota
    return suma

lista_notas = []
lista_notas.append(float(input("Ingrese una nota (CERO para salir): ")))


while (lista_notas[len(lista_notas) - 1] > 0):
    print(len(lista_notas))
    lista_notas.append(float(input("Ingrese una nota (CERO para salir): ")))

lista_notas.pop(len(lista_notas) - 1)

if (len(lista_notas) > 0):
    promedio = sumar_notas(lista_notas) / len(lista_notas)

    print("Notas: ", lista_notas)
    print("El promedio es: ", promedio)
"""