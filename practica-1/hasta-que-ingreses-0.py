# Programa que suma números ingresados por el usuario hasta que ingrese 0

suma=0  

while True:
    numero = int(input("Introduce un número (ingresa 0 para detener): "))
    if numero == 0:
        break  # Si el número es 0, termina el bucle
    suma += numero  

print("La suma total es:", suma)