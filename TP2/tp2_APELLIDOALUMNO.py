#PROFESOR: MAXIMILIANO PERELLÓN
#ALUMNO: Maximo Gomez

#           TRABAJO PRACTICO Nº2 - CONDICIONALES

#PARA COMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + C

#PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + U

#Ejercicio 1
# edad_del_usuario = int(input("Ingresa tu edad: "))
# if edad_del_usuario >= 18:
#     print("Eres mayor de edad.")
# else:
#     print("Eres menor de edad.")



#Ejercicio 2
# dinero = int(input("Ingrese el numero 100 o un numero mayor: "))
# if dinero == 100:
#     print("usted pago en efectivo")
# elif dinero >= 300:
#     print("Usted pago con tarjeta de credito")
# else:
#     print("Usted pago con tarjeta de debito")
#Ejercicio 3
# numeroa=float(input("ingrese a dividir: "))
# numerob=float(input("ingrese el divisor: "))
# if numerob == 0:
#     print("Error no se puede dividir")
# else:
#     numeroc=numeroa/numerob
#     print("El resultado de la division  es", numeroc)

#Ejercicio 4
# numero = int(input("Introduce un número entero: "))
# if numero % 2 == 0:
#     print("El número", numero, "es par.")
# else:
#     print("El número", numero, "es impar.")


#Ejercicio 5
# edad = int(input("ingresa tu edad: "))
# if edad < 4:
#     precio = 0  
# elif 4 <= edad <= 18:
#     precio = 200  
# else:
#     precio = 500  
# print("El precio de la entrada es de: ",  (precio))


#Ejercicio 6
# numero = float(input("Por favor, ingresa un número: "))
# if numero > 0:
#     print("El número ingresado es positivo.")
# elif numero < 0:
#     print("El número ingresado es negativo.")
# else:
#     print("El número ingresado es cero.")


#Ejercicio 7
# num1 = int(input("Ingresa el primer número entero: "))
# num2 = int(input("Ingresa el segundo número entero: "))
# num3 = int(input("Ingresa el tercer número entero: "))
# if num1 >= num2 and num1 >= num3:
#     mayor = num1
# elif num2 >= num1 and num2 >= num3:
#     mayor = num2
# else:
#     mayor = num3
# print("El mayor de los tres números es:", mayor)


#Ejercicio 8
# numero1 = int(input("Ingresa el primer número: "))
# numero2 = int(input("Ingresa el segundo número: "))
# if numero1 % numero2 == 0:
#     print(numero1, "es múltiplo de", numero2)
# else:
#     print(numero1, "no es múltiplo de", numero2)


#Ejercicio 9
# numero = int(input("Ingresa un número del 1 al 7: "))
# if numero == 1:
#     dia = "Lunes"
# elif numero == 2:
#     dia = "Martes"
# elif numero == 3:
#     dia = "Miércoles"
# elif numero == 4:
#     dia = "Jueves"
# elif numero == 5:
#     dia = "Viernes"
# elif numero == 6:
#     dia = "Sábado"
# elif numero == 7:
#     dia = "Domingo"
# else:
#     dia = "Número inválido (debe ser del 1 al 7)"
# print("El día correspondiente al número", numero, "es", dia)


#Ejercicio 10
# caracter = input("Ingresa un carácter: ")
# if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
#     print("El carácter ingresado es una vocal.")
# else:
#     print("El carácter ingresado es una consonante.")
