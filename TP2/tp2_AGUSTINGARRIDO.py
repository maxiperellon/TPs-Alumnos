#PROFESOR: MAXIMILIANO PERELLON
#ALUMNO: AGUSTIN GARRIDO

#           TRABAJO PRACTICO N2 - CONDICIONALES

#PARA COMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + C

#PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + U

#Ejercicio 1
#codigo
#edad = int(input("Por favor, introduce tu edad: "))

#if edad >= 18:
#    print("Eres mayor de edad.")
#else:
#    print("No eres mayor de edad.")
#Ejercicio 2
#codigo

#asto = float(input("Por favor, introduce la cantidad que has gastado: "))

#if gasto <= 100:
 #   print("Paga con dinero en efectivo.")
#elif gasto > 100 and gasto < 300:
 #   print("Paga con tarjeta de débito.")
#else:
    #print("Paga con tarjeta de crédito.")


#Ejercicio 3
#codigo
#num1 = float(input("Por favor, introduce el primer número (dividendo): "))
#num2 = float(input("Por favor, introduce el segundo número (divisor): "))
#if num2 == 0:
#    print("Error: El divisor no puede ser cero.")
#else:
#    division = num1 / num2
#    print(f"La división de {num1} entre {num2} es {division}.")
#Ejercicio 4
#codigo
#numero = int(input("Por favor, introduce un número entero: "))

#if numero % 2 == 0:
#    print("El número es par.")
#else:
#    print("El número es impar.")


#Ejercicio 5
#codigo
# Pregunta al usuario la edad del cliente
#edad = int(input("Por favor, introduce la edad del cliente: "))

# Decide el precio de la entrada
#if edad < 4:
#    print("El cliente puede entrar gratis.")
#elif edad >= 4 and edad <= 18:
#    print("El precio de la entrada es $200.")
#else:
#    print("El precio de la entrada es $500.")

#Ejercicio 6
#codigo
# Pregunta al usuario un número
#numero = float(input("Por favor, introduce un número: "))

# Verifica si el número es positivo, negativo o cero
#if numero > 0:
#    print("El número es positivo.")
#elif numero < 0:
 #   print("El número es negativo.")
#else:
#    print("El número es cero.")

#Ejercicio 7
#codigo
# Pregunta al usuario tres números enteros
#num1 = int(input("Por favor, introduce el primer número: "))
#num2 = int(input("Por favor, introduce el segundo número: "))
#num3 = int(input("Por favor, introduce el tercer número: "))

# Encuentra y muestra el número mayor
#Mayor = max(num1, num2, num3)
#print(f"El número mayor es {mayor}.")

#Ejercicio 8
#codigo

#num1 = int(input("Por favor, introduce el primer número: "))
#num2 = int(input("Por favor, introduce el segundo número: "))

#if num1 % num2 == 0:
#    print(f"{num1} es múltiplo de {num2}.")
#else:
#    print(f"{num1} no es múltiplo de {num2}.")

#Ejercicio 9
#codigo
#numero = int(input("Por favor, introduce un número del 1 al 7: "))
#dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

#if 1 <= numero <= 7:
#    print(f"El día de la semana correspondiente al número {numero} es {dias_semana[numero - 1]}.")
#else:
#    print("Error: El número debe estar entre 1 y 7.")

#Ejercicio 10
#codigo
#caracter = input("Por favor, introduce un carácter: ")

#vocales = ["a", "e", "i", "o", "u"]

#if caracter.lower() in vocales:
#    print(f"El carácter {caracter} es una vocal.")
#else:
    #print(f"El carácter {caracter} es una consonante.")
