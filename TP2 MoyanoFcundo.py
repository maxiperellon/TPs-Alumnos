#PROFESOR: MAXIMILIANO PERELLÓN
#ALUMNO: ....

#           TRABAJO PRACTICO Nº2 - CONDICIONALES

#PARA COMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + C

#PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + U

#Ejercicio 1
#codigo

""" edad = int(input("ingrese su edad"))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("No eres mayor de edad.") """

#Ejercicio 2
#codigo

""" gasto = float(input("Ingresa la cantidad gastada: "))
if gasto <= 100:
    print("Paga con dinero en efectivo.")
elif gasto > 100 and gasto < 300:
    print("Paga con tarjeta de débito.")
else:
    print("Paga con tarjeta de crédito.") """

#Ejercicio 3
#codigo
""" 
dividendo = float(input("Ingresa el dividendo: "))
divisor = float(input("Ingresa el divisor: "))
if divisor == 0:
    print("Error: El divisor no puede ser cero.")
else:
    division = dividendo / divisor
    print("El resultado de la división es: ", division) """

#Ejercicio 4
#codigo

""" numero = int(input("Ingresa un número entero: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.") """

#Ejercicio 5
#codigo

""" edad = int(input("Ingresa la edad del cliente: "))
if edad < 4:
    print("El cliente puede entrar gratis.")
elif edad >= 4 and edad <= 18:
    print("El precio de la entrada es de $200.")
else:
    print("El precio de la entrada es de $500.") """

#Ejercicio 6
#codigo

""" numero = float(input("Ingresa un número: "))
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.") """

#Ejercicio 7
#codigo

""" numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))
mayor = max(numero1, numero2, numero3)
print("El mayor de los números ingresados es: ", mayor) """

#Ejercicio 8
#codigo

""" numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
if numero1 % numero2 == 0:
    print("El primer número es múltiplo del segundo.")
else:
    print("El primer número no es múltiplo del segundo.") """

#Ejercicio 9
#codigo

""" numero = int(input("Ingresa un número del 1 al 7: "))
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
if 1 <= numero <= 7:
    print("El día de la semana es: ", dias_semana[numero - 1])
else:
    print("Error: Debes ingresar un número del 1 al 7.") """

#Ejercicio 10
#codigo

""" caracter = input("Ingresa un carácter: ")
if caracter.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("El carácter ingresado es una vocal.")
elif caracter.isalpha():
    print("El carácter ingresado es una consonante.")
else:
    print("Error: Debes ingresar un carácter alfabético.") """