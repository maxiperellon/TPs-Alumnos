#PROFESOR: MAXIMILIANO PERELLON
#ALUMNO:Valentino Calvo

#           TRABAJO PRACTICO Nº3 BUCLES

#PARA COMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + C

#PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + U

#Ejercicio 1
#codigo

# La función range() en Python es una función incorporada que se utiliza para generar una secuencia de números. 
# Esta función es muy útil cuando necesitas iterar sobre una secuencia de números, como en un bucle for.

# for i in range(1, 11):
#     print(i)


#Ejercicio 2
#codigo

# La función len() es una función incorporada en Python que se utiliza para obtener el número de elementos en un objeto. 

# numeros = [10, 8, 7, 9, 9]
# suma = 0
# for num in numeros:
#     suma += num
# promedio = suma / len(numeros)
# print("El promedio es:", promedio)



#Ejercicio 3
#codigo

# num = int(input("Por favor ingrese un número: "))
# i = 2
# while i <= num:
#     print(i)
#     i += 2

#Ejercicio 4
#codigo

# palabra = input("Por favor ingrese una palabra: ")
# for letra in palabra:
#     print(letra)

#Ejercicio 5
#codigo

# num = int(input("Por favor ingrese un número entero positivo: "))
# suma = 0
# for i in range(1, num + 1):
#     if i % 2 != 0:
#         suma += i
# print("La suma de los números impares entre 1 y", num, "es", suma)


#Ejercicio 6
#codigo

# num = int(input("Por favor ingrese un número entero positivo: "))
# suma = 0
# i = 2
# while i <= num:
#     suma += i
#     i += 2
# print("La suma de los números pares entre 2 y", num, "es", suma)

#Ejercicio 7
#codigo

# La función split() es una función muy útil en programación que se utiliza para dividir una cadena de texto (string) 
# en una lista de subcadenas

# numeros = input("Por favor, ingresa una serie de números enteros separados por espacios: ")
# numeros = numeros.split()
# pares = 0
# impares = 0
# for numero in numeros:
#     numero = int(numero)
#     if numero % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
# print("Cantidad de números pares: ", pares)
# print("Cantidad de números impares: ", impares)

#Ejercicio 8
#codigo

# num = int(input("Introduce un número entero: "))
# i = 1
# while i <= 10:
#     print(num, "x", i, "=", num * i)
#     i += 1