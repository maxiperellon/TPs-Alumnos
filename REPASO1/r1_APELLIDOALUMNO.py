#PROFESOR: MAXIMILIANO PERELLON
#ALUMNO: ....

#           REPASO Nº1 CONDICIONALES - BUCLES

#PARA COMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + C

#PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + U

#Ejercicio 1
#codigo

# for i in range(1, 11):
#     print(i)


#Ejercicio 2
#codigo

# for i in range(2, 21, 2):
#     print(i)

#Ejercicio 3
#codigo

# numero = float(input("Por favor, ingrese un número: "))
# if numero > 0:
#     print("El número es positivo.")
# elif numero < 0:
#     print("El número es negativo.")
# else:
#     print("El número es cero.")

#Ejercicio 4
#codigo

# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("HolaChau")
#     elif i % 3 == 0:
#         print("Hola")
#     elif i % 5 == 0:
#         print("Chau")
#     else:
#         print("Este número no es múltiplo:")

#Ejercicio 5
#codigo

# cadena = input("Por favor, ingrese una cadena de texto: ")
# if "a" in cadena:
#     print("La cadena contiene la letra 'a'.")
# else:
#     print("La cadena no contiene la letra 'a'.")

#Ejercicio 6
#codigo

# cadena = input("Por favor, ingrese una cadena de texto: ")
# vocales = 0
# for letra in cadena:
#     if letra in "aeiouAEIOU":
#         vocales += 1
# print("La cadena contiene", vocales, "vocales.")

#Ejercicio 7
#codigo

# contraseña_correcta = "1234"
# intentos = 0
# while intentos < 3:
#     contraseña = input("Por favor, ingrese su contraseña: ")
#     if contraseña == contraseña_correcta:
#         print("La contraseña es correcta.")
#         break
#     else:
#         print("La contraseña es incorrecta. Inténtalo de nuevo.")
#         intentos += 1

# if intentos == 3:
#     print("Has alcanzado el máximo de intentos.")


