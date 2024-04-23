#PROFESOR: MAXIMILIANO PERELLON
#ALUMNO: ....

#           TRABAJO PRACTICO Nº3 BUCLES

#PARA COMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + C

#PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + U

#Ejercicio 1
#codigo

""" for i in range(1, 11):
    print(i) """

#Ejercicio 2
#codigo

""" numeros = [4, 2, 9, 7, 5, 1]
suma = 0
for numero in numeros:
    suma += numero
promedio = suma / len(numeros)
print("El promedio es: ", promedio) """

#Ejercicio 3
#codigo

""" numero = int(input("Ingresa un número: "))
contador = 2
while contador <= numero:
    print(contador)
    contador += 2 """

#Ejercicio 4
#codigo

""" palabra = input("Ingresa una palabra: ")
for letra in palabra:
    print(letra) """

#Ejercicio 5
#codigo

""" numero = int(input("Ingresa un número entero positivo: "))
suma = 0
for i in range(1, numero + 1):
    if i % 2 != 0:
        suma += i
print("La suma de los números impares entre 1 y {} es: {}".format(numero, suma)) """

#Ejercicio 6
#codigo

""" numero = int(input("Ingresa un número entero positivo: "))
suma = 0
contador = 2
while contador <= numero:
    suma += contador
    contador += 2
print("La suma de los números pares entre 2 y {} es: {}".format(numero, suma)) """

#Ejercicio 7
#codigo

""" numeros = input("Ingresa una serie de números enteros separados por espacios: ")
numeros = numeros.split()
pares = 0
impares = 0
for numero in numeros:
    numero = int(numero)
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
print("Cantidad de números pares: ", pares)
print("Cantidad de números impares: ", impares) """

#Ejercicio 8
#codigo

""" numero = int(input("Ingresa un número entero: "))
contador = 1
while contador <= 10:
    print("{} x {} = {}".format(numero, contador, numero * contador))
    contador += 1 """