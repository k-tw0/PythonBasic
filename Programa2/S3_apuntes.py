#   EJERCICIO 1 
#   Si la cantidad de años que cumplirá el usuario es igual a 18, entonces
#   mostrará un mensaje adicional que diga “Pronto serás mayor de edad”,
#   por el contrario, si los años que cumplirá no son 18, que no muestre ese
#   mensaje extra.
    

"""
A partir de ahora a un if lo llamaremos instrucción condicional y
aprenderemos con un ejemplo la forma de emplearlo y cómo trabaja.

edad = int(input("Ingrese su edad: "))
edad = edad + 1
if (edad == 18 ):
    print("Pronto sera mayor de edad")
print("Cumpliras", edad, "años")

"""

#   EJERCICIO 2

#   Pediremos al usuario que ingrese el monto de su salario. Si el monto es
#   igual o superior a los $500.000, entonces deberá pagar un seguro por
#   El bloque if para cuando la condición es verdadera y el bloque else para
#   $15.000. Si, por el contrario, su salario es menor a $500.000 el seguro le
#   costará $ 8.000.

"""

cuando la condición es falsa.

la declaración if-else nos brinda dos caminos de
ejecución dentro de nuestro flujo. Veámoslo con un ejemplo:


salario = int(input("Ingrese el monto del salario que percibe: "))
if(salario >= 500000):
    print("Debe pagar $15.000 por concepto de seguros")
else:
    print("Debe pagar $8.000 por concepto de seguros")

"""

#   EJERCICIO 3

#   Supongamos que cambian las condiciones del cobro de seguro de
#   nuestro ejemplo anterior, ahora los salarios de $500.000 o más pagan el
#   2% del salario multiplicado por los años de antigüedad. Los salarios
#   menores a $500.000 pagan por concepto de seguro sólo el 1.2%
#   multiplicado por los años de antigüedad.

"""

def calcular_seguro(monto_salario, anios_antiguedad, porcentaje):
    a_pagar = (monto_salario * porcentaje / 100) * anios_antiguedad
    return a_pagar

salario = int(input("Ingrese el monto del salario que percibe: "))
antiguedad = int(input("Ingrese los años de antiguedad: "))

if(salario >= 500000):
    monto_seguro = calcular_seguro(salario, antiguedad, 2)
else:
    monto_seguro = calcular_seguro(salario, antiguedad, 1.2)
print("Debes pagar $", monto_seguro, "por concepto de seguros")

"""

#   EJERCICIO 4

#   En otras situaciones podremos necesitar hacer uso de la anidación de
#   declaraciones if o if-else, lo que en estricto rigor significa poder hacer
#   una pregunta dentro de otra pregunta e ir ramificando los posibles
#   caminos de la ejecución de un programa.

"""

edad = int(input("Ingrese su edad: "))
if (edad < 18):
    estatura = float(input("Ingrese su estura: "))
    if (estatura < 1.5):
        print("Necesita la compañia de un adulto para ingresar")
    else:
        print("Puede ingresar sin compañia")
print("Bienvenido al parque")

"""





