#PROFESOR: MAXIMILIANO PERELLON
#ALUMNO: ....

#           TRABAJO PRACTICO Nº3 BUCLES

#PARA COMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + C

#PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + U

#Ejercicio 1
# for x in range (1,11):
#     print(x)

# #Ejercicio 2
# numeros = [1, 2, 3, 4, 5]
# suma = 0

# for numero in numeros:
#     suma += numero

# promedio = suma / len(numeros)
# print("El promedio es:", promedio)

#Ejercicio 3
# numero = int(input("Ingrese un numero: "))
# i = 2
# while i <= numero:
#     if i % 2 == 0:
#         print(i)
#     i += 1

#Ejercicio 4
# palabra = input("Ingrese una palabra: ")
# for letra in palabra:
#     print(letra)

# #Ejercicio 5
# numero = int(input("Ingrese un numero entero positivo: "))
# i = 1
# while i <= numero:
#     if i % 2 != 0:
#         print(i)
#     i += 1

# #Ejercicio 6
# numero = int(input("Ingrese un numero entero positivo: "))
# suma = 0
# i = 2
# while i <= numero:
#     suma += i
#     i += 2
# print("La suma de los números pares es:", suma)

# #Ejercicio 7

# serie_numeros = input("Ingrese una serie de números enteros separados por espacios: ")
# numeros = serie_numeros.split()
# pares = 0
# impares = 0
# for numero in numeros:
#     numero = int(numero)    
#     if numero % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
# print("Cantidad de números pares:", pares)
# print("Cantidad de números impares:", impares)

#Ejercicio 8
# numero = int(input("Ingrese un número entero: "))
# contador = 1
# print("Tabla de multiplicar del", numero, ":")
# while contador <= 10:
#     resultado = numero * contador
#     print(numero, "x", contador, "=", resultado)
#     contador += 1
