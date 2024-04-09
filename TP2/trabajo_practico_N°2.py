#PROFESOR:  MAXIMILIANO PERELLÓN
#ALUMNO: Valentino calvo 

#           TRABAJO PRACTICO Nº2 - CONDICIONALES

#PARA COMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + C

#PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + U

#Ejercicio 1Escribir un programa que pregunte al usuario su edad y muestre por pantalla si
# es mayor de edad o no.

#codigo:
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# x = int(input("Ingrese su x: "))
# if x >= 18:
#     print("Usted es mayor de x.")
# else:
#     print("Usted no es mayor de x.")

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Ejercicio 2
#  Si gasto hasta $100, pago con dinero en efectivo. Sino, si gasto más de $100 
# pero menos de $300, pago con tarjeta de débito. Sino, pago con tarjeta de crédito.
#codigo:
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# x = float(input("Ingrese el x de su compra: "))
# if x <= 100:
#     print("Pago en efectivo.")
# elif 100 < x < 300:
#     print("Pago con tarjeta de débito.")
# else:
#     print("Pago con tarjeta de crédito.")
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Ejercicio 3
# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# “Si el divisor es cero el programa debe mostrar un error”.
#codigo:
#  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Ejercicio 3
# lolsito1 = float(input("Ingrese el primer número: "))
# lolsito2 = float(input("Ingrese el segundo número: "))
# if lolsito2 != 0:
#     print("La división es:", lolsito1 / lolsito2)
# else:
#     print("Error: El divisor no puede ser cero.")
#  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Ejercicio 4
# Escribir un programa que pida al usuario un número entero y
#  muestre por pantalla si es par o impar.

#codigo:
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# x = int(input("Ingrese un número entero: "))
# if x % 2 == 0:
#     print("El número es par.")
# else:
#     print("El número es impar.")


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Ejercicio 5
# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y 
# quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $200 y
# si es mayor de 18 años, $500.
#codigo:
# //////////////////////////////////////////////////////////////////////////////////////////////
# persona = int(input("Ingrese la edad del cliente: "))
# if persona < 4:
#     print("El cliente puede entrar gratis.")
# elif 4 <= persona <= 18:
#     print("El cliente debe pagar $200.")
# else:
#     print("El cliente debe pagar $500.")






# //////////////////////////////////////////////////////////////////////////////////////////////

# Ejercicio 6:Escribe un programa que solicite al usuario ingresar un número y 
# determine si es positivo, negativo o cero.
#codigo:
# //////////////////////////////////////////////////////////////////////////////////////////////

# numero = float(input("Ingrese un número: "))
# if numero > 0:
#     print("El número es positivo.")
# elif numero < 0:
#     print("El número es negativo.")
# else:
#     print("El número es cero.")


# //////////////////////////////////////////////////////////////////////////////////////////////

# Ejercicio 7:Escribe un programa que pida al u
# suario ingresar tres números enteros y muestre por pantalla el mayor de ellos
#codigo:
# //////////////////////////////////////////////////////////////////////////////////////////////

# x1 = int(input("Ingrese el primer número: "))
# x2 = int(input("Ingrese el segundo número: "))
# x3 = int(input("Ingrese el tercer número: "))
# lol = x1
# if x2 > lol:
#     lol = x2
# if x3 > lol:
#     lol = x3
# print("El mayor número es:", lol)


# //////////////////////////////////////////////////////////////////////////////////////////////

# .Ejercicio 8:Escribe un programa que solicite al usuario ingresar dos números y
# determine si el primero es múltiplo del segundo.
#codigo:
# //////////////////////////////////////////////////////////////////////////////////////////////

# x1 = int(input("Ingrese el primer número: "))
# x2 = int(input("Ingrese el segundo número: "))
# if x1 % x2 == 0:
#     print("El primer número es múltiplo del segundo.")
# else:
#     print("El primer número no es múltiplo del segundo.")


# //////////////////////////////////////////////////////////////////////////////////////////////
# Ejercicio 9:Escribe un programa que solicite al usuario ingresar un número del 1 al 7 y
# muestre por pantalla el día de la semana correspondiente (1 para Lunes, 2 para Martes, etc.)
#codigo:
# //////////////////////////////////////////////////////////////////////////////////////////////

# dia = int(input("Ingrese un número del 1 al 7: "))
# if dia == 1:
#     print("Lunes")
# elif dia == 2:
#     print("Martes")
# elif dia == 3:
#     print("Miércoles")
# elif dia == 4:
#     print("Jueves")
# elif dia == 5:
#     print("Viernes")
# elif dia == 6:
#     print("Sábado")
# elif dia == 7:
#     print("Domingo")
# else:
#     print("Número inválido.")

# //////////////////////////////////////////////////////////////////////////////////////////////


# .Ejercicio 10:Escribe un programa que solicite al usuario ingresar un carácter y determine 
# si es una vocal (a, e, i, o, u) o una consonante.
#codigo:

# //////////////////////////////////////////////////////////////////////////////////////////////

# letra = input("Ingrese un carácter: ")
# if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
#     print("El carácter ingresado es una vocal.")
# else:
#     print("El  carácter ingresado es una consonante.")


# //////////////////////////////////////////////////////////////////////////////////////////////






