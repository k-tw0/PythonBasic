#   EJERCICIO 1
#Enunciado: Mostrar por pantalla todos los números pares comprendidos
#entre los números 2 y 20.

"""
for par in range(2, 21, 2):
    print(par)
"""

#   EJERCICIO 2

#   Distinto de 0
#   Utilizando ciclo while

"""

notas = []  #   Listado de notas
sumatoria = 0
nota = int(input("Ingrese nota (cero para salir):"))
while (nota != 0): # Si es distinto de 0
    notas.append(nota)
    nota = int(input("Ingrese nota (cero para salir): "))
if (len(notas) != 0):
    for item  in notas:
        sumatoria = sumatoria + item
    print("El promedio es: ", sumatoria/len(notas))
print("Gracias por utilizar nuestro programa")

"""

"""

Para que no nos falten ejemplos, si quisiéramos cambiar el valor del
segundo elemento de nuestra Lista1, que es un 42, y en su lugar colocar
un 33, debemos utilizar el índice de la posición, sabiendo que lista
comienza en la posición cero, la segunda posición tiene el índice 1.
Entonces, Lista1[1] = 33

"""

# EJERCICIO 3

#Ejercicio de ordenamiento de elementos:
#Dada una lista llamada L con 3 elementos en su interior [6, 2, 8], se
#necesita un programa que sea capaz de ordenar los valores de menor
#a mayor dentro de la lista.
#Para este tipo de ejercicios se requerirá de una variable auxiliar que
#permita intercambiar los valores de posición sin que se pierdan.
#A continuación, lo resolveremos sólo con declaraciones if y después lo
#haremos aplicando un bucle for.

"""
L = [6, 2, 8]
# Si L en la posicion 0(6) es mayor que la posicion 1(2)
    # variable Aux(6) es igual a L en la posicion 0(6)
    # L en la posicion 0(2) es igual a la posicion L en la posicion 1(2)
    # L en la posicion 1(2) es igual a Aux(6)

if L[0]>L[1]:
    Aux = L[0]
    L[0] = L[1]
    L[1] = Aux

if L[1]>L[2]:
    Aux = L[1]
    L[1] = L[2]
    L[2] = Aux

print(L)

"""

# EJERCICIO 4
# Ciclo for para ordenar de mayor a menor.

"""

Interpretemos los argumentos de range. Desde 0 hasta len(L)-1, la
longitud de L es de 3, menos 1 es igual a 2. Desde 0 hasta 2 con paso 1.
Entonces for está manejando las posiciones de la lista [0], [1] y [2] en la
variable pos y de ese modo comparar y reemplazar los valores.
Para 3 valores, el ordenamiento y los posibles intercambios son
relativamente pocos y fáciles de aplicar con if o con for.

L = [6, 2, 8]
print(len(L) -1)
for pos in range(0, len(L) -1,1): #   Para posicion en un rango de 0, [L tiene 3 posiciones pero en realidad son 2 y restamos 1], conteo de 1 en 1.
    print("Pos:", pos, "L[pos]: ",L[pos],"L[pos+1]:", L[pos+1], "L[pos] > L[pos+1]", L[pos] > L[pos+1])
    if L[pos] > L[pos+1]: #   Si L (Posicion) es mayor que L(posicion + 1)
        Aux = L[pos]
        L[pos] = L[pos+1]
        L[pos+1] = Aux
print(L)
"""
#En este punto tal vez nos estemos pasando el límite de principiante hacia
#avanzado, manejar bucles anidados es algo que requiere algo de
#destreza y práctica. Pero es bueno comenzar a visualizar las utilidades
#que podría tener

"""

R = [3, 2, 8, 5, 1, 7]
for i in range(1, len(R), 1):
    for j in range(0,len(R)-i,1):
        if R[j] > R[j+1]:
            Aux = R[j]
            R[j] = R[j+1]
            R[j+1] = Aux
print(R)

"""