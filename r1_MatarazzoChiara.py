#PROFESOR: MAXIMILIANO PERELLON
#ALUMNO: Chiara Matarazzo

#           REPASO Nº1 CONDICIONALES - BUCLES

#PARA COMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + C

#PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + U

# #Ejercicio 1
# for i in range(1, 11):
#     print(i)

# #Ejercicio 2
# #for i in range(2, 21, 2):
#     print(i)

# #Ejercicio 3
# #numero = int(input("Ingrese un número: "))
# if numero > 0:
#     print("El número es positivo")
# elif numero < 0:
#     print("El número es negativo")
# else:
#     print("El número es cero")

# #Ejercicio 4
# #for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("HolaChau")
#     elif i % 3 == 0:
#         print("Hola")
#     elif i % 5 == 0:
#         print("Chau")
#     else:
#         print("este número no es múltiplo", i)

# #Ejercicio 5
# #cadena = input("Ingrese una cadena de texto: ")
# if "a" in cadena:
#     print("La cadena contiene la letra 'a'")
# else:
#     print("La cadena no contiene la letra 'a'")

# #Ejercicio 6
# #cadena = input("Ingrese una cadena de texto: ")
# vocales = 0
# for letra in cadena:
#     if letra.lower() in "aeiou":
#         vocales += 1
# print("La cantidad de vocales encontradas es:", vocales)

# #Ejercicio 7
# #intentos_maximos = 3
# intentos_restantes = intentos_maximos
# contrasena_correcta = "secreto"
# while intentos_restantes > 0:
#     contrasena_ingresada = input("Ingrese la contraseña: ")
#     if contrasena_ingresada == contrasena_correcta:
#         print("Contraseña correcta!")
#         break
#     else:
#         intentos_restantes -= 1
#         if intentos_restantes == 0:
#             print("Lo siento, se ha alcanzado el límite de intentos.")
#         else:
#             print("Contraseña incorrecta. Te quedan " + str(intentos_restantes) + " intentos.")
