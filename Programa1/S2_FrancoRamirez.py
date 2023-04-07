# By: FRANCO LEANY RAMIREZ LIEVA
# Weakle: SEMANA 2
# Teacher: Eder Patricio Moran Heredia
#nombre = "Franco"

# 1 [CALCULAR UNA SUMA]

# Entradas
num1 = int(input("Ingrese el 1er numero: "))
num2 = int(input("Ingrese el 2do numero: "))

# Procesos
resultado = num1 + num2
print("El resultado de la suma:",resultado)

# 2 [CALCULAR UNA SUMA CON FUNCION]

# Funcion con parametro
def sumar(n1, n2):
    result = n1 + n2
    return result

# Entrada
n1 = int(input("Ingrese el 1er numero: "))
n2 = int(input("Ingrese el 2do numero: "))

# Proceso
result = sumar(n1,n2)

# Salida
print("El resultado de la funncion:", result)


# 3 [CALCULAR AREA RECTANGULO]

# Funcion con parametro
def calcula_area_rect(b, a):
    ar = a * b
    return ar

# Entrada
base = float(input("Ingrese la base del rectangulo:"))
altura = float(input("Ingrese la altura del rectangulo:"))

# Proceso
resultArea = calcula_area_rect(base,altura)

# Salida
print("El area del rectangulo es: ", resultArea)