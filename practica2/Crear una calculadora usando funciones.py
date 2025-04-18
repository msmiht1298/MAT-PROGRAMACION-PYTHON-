# Definir funciones para las operaciones
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"

# Solicitar números y operación al usuario
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
operacion = input("Elige la operación (sumar/restar/multiplicar/dividir): ")

# Realizar la operación
if operacion == "sumar":
    resultado = sumar(numero1, numero2)
elif operacion == "restar":
    resultado = restar(numero1, numero2)
elif operacion == "multiplicar":
    resultado = multiplicar(numero1, numero2)
elif operacion == "dividir":
    resultado = dividir(numero1, numero2)
else:
    resultado = "Operación no válida"

print("El resultado es:", resultado)
