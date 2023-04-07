# By: FRANCO LEANY RAMIREZ LIEVA
# Weakle: SEMANA 2
# Teacher: Eder Patricio Moran Heredia

# Funcion con parametro
#variable decada
decada = 10
def calcularEdad(ed):
    result = ed + decada
    return result

# Entrada
nombre = str(input("Ingrese su nombre: "))
edad = int(input("Ingrese su cantidad de años en este mundo: "))


# Proceso
result = calcularEdad(edad)

# Salida
print("Estimado,",nombre, "en una década su edad será de", result, "años.")

