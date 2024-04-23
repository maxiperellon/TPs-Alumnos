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
# suma = 0
# while i <= numero:
#     if i % 2 != 0:
#         suma += i
#     i += 1
# print("La suma de los números impares es:", suma)


# #Ejercicio 6
# numero = int(input("Ingrese un numero entero positivo: "))
# suma = 0
# i = 2
# while i <= numero:
#     suma += i
#     i += 2
# print("La suma de los números pares es:", suma)

# #Ejercicio 7

# numeros = input("Ingrese una serie de números enteros separados por espacios: ")
# pares = 0
# impares = 0
# numeros2 = numeros.split()
# for num in numeros2:
#     if int(num) % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
# print("Cantidad de números pares:", pares)
# print("Cantidad de números impares:", impares)


# #Ejercicio 8
# numero = int(input("Ingrese un número entero: "))
# i = 1
# print("Tabla de multiplicar del", numero, ":")
# while i <= 10:
#     resultado = numero * i
#     print(numero, "x", i, "=", resultado)
#     i += 1
