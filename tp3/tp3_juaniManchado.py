#PROFESOR: MAXIMILIANO PERELLON
#ALUMNO: Juani Chado

#           TRABAJO PRACTICO Nº3 BUCLES

#PARA COMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + C

#PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + U

#Ejercicio 1
#codigo
print("Ejercicio 1:")
for i in range(1, 11):
    print(i)
#Ejercicio 2
#codigo
print("\nEjercicio 2:")
lista_numeros = [5, 8, 12, 6, 10]
suma = 0
for num in lista_numeros:
    suma += num
promedio = suma / len(lista_numeros)
print("El promedio de la lista es:", promedio)
#Ejercicio 3
#codigo
print("\nEjercicio 3:")
numero = int(input("Ingrese un número: "))
i = 2
while i <= numero:
    print(i)
    i += 2
#Ejercicio 4
#codigo
print("\nEjercicio 4:")
palabra = input("Ingrese una palabra: ")
for letra in palabra:
    print(letra)
#Ejercicio 5
#codigo
print("\nEjercicio 5:")
numero = int(input("Ingrese un número entero positivo: "))
suma_impares = 0
for i in range(1, numero + 1, 2):
    suma_impares += i
print("La suma de los números impares hasta", numero, "es:", suma_impares)
#Ejercicio 6
#codigo
print("\nEjercicio 6:")
numero = int(input("Ingrese un número entero positivo: "))
suma_pares = 0
i = 2
while i <= numero:
    suma_pares += i
    i += 2
print("La suma de los números pares hasta", numero, "es:", suma_pares)
#Ejercicio 7
#codigo
print("\nEjercicio 7:")
numeros = input("Ingrese una serie de números enteros separados por espacios: ")
numeros_separados = numeros.split()
pares = 0
impares = 0
for num in numeros_separados:
    if int(num) % 2 == 0:
        pares += 1
    else:
        impares += 1
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
#Ejercicio 8
#codigo
print("\nEjercicio 8:")
numero = int(input("Ingrese un número entero: "))
i = 1
while i <= 10:
    print(numero, "x", i, "=", numero * i)
    i += 1