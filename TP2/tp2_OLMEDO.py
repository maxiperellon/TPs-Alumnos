#PROFESOR: MAXIMILIANO PERELLÓN
#ALUMNO: ....

#           TRABAJO PRACTICO Nº2 - CONDICIONALES

#PARA COMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + C

#PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + U

#Ejercicio 1
# edad = int(input("Ingrese su edad: "))
# if edad >= 18:
#     print("Eres mayor de edad")
# elif edad < 18:
#     print("Eres menor de edad")

#Ejercicio 2
# saldo = int(input("Saldo a pagar: "))
# if saldo <= 100:
#     print("Pago con efectivo")
# elif saldo >100 and saldo <300:
#     print("Pago con tarjeta de debito")
# else:
#     print("Pago con tarjeta de credito")
    
#Ejercicio 3
# numero1 = float(input("Ingrese un numero: "))
# numero2 = float(input("Ingrese un numero: "))

# if numero2 == 0:
#     print("No hay numero divisible por 0")
# else:
#     division = numero1/numero2
#     print("La división de", numero1, "entre", numero2, "es:", division)

#Ejercicio 4
# nument = int(input("Ingrese un numero entero: "))
# if nument % 2 == 0:
#     print(nument,"El numero es par")
# else:
#     print(nument,"El numero es impar")

#Ejercicio 5
# edad = int(input("Ingrese su edad: "))
# if edad < 4:
#     print("Su entrada es gratis")
# elif edad >= 4 and edad < 18:
#     print("Pague 200 pesos")
# elif edad >= 18:
#     print("Pague 500 pesos")

#Ejercicio 6
# numero = float(input("Ingrese un numero: "))
# if numero == 0:
#     print("El numero ingresado es cero")
# elif numero < 0:
#     print("El numero ingresado es negativo")
# elif numero > 0:
#     print("El numero ingresado es positivo")
#Ejercicio 7
# numero1 = int(input("Ingrese un numero: "))
# numero2 = int(input("Ingrese un numero: "))
# numero3 = int(input("Ingrese un numero: "))
# if numero1 > numero2 and numero3:
#     print (numero1, "Este nuemro es el mayor de todos ")
# elif numero2 > numero1 and numero3:
#     print(numero2, "Este numero es el mayor de todos")
# elif numero3 > numero1 and numero2:
#     print(numero3, "Este nuemro es el mayor de todos ")

#Ejercicio 8
# numero1 = float(input("Ingrese un numero: "))
# numero2 = float(input("Ingrese un numero: "))
# if numero1 % numero2 == 0:
#     print(numero1, "Este numero es multiplo de", numero2)
# else:
#     print(numero1, "Este numero no es multiplo de", numero2)

#Ejercicio 9
# numero = float(input("Ingrese un numero del 1 al 7: "))
# if numero == 1:
#     print("Lunes")
# elif numero == 2:
#     print("Martes")
# elif numero == 3:
#     print("Miercoles")
# elif numero == 4:
#     print("Jueves")
# elif numero == 5:
#     print("Viernes")
# elif numero == 6:
#     print("Sabado")
# elif numero == 7:
#     print("Domingo")

#Ejercicio 10
# letra = str(input("Ingrese una letra: "))
# if letra == "a" or "e" or "i" or "o" or "u":
#     print ("Es una vocal")
# elif letra == "b" or "c" or "d" or "f" or "g" or "h" or "j" or "k" or "l" or "m" or "n" or "p" or "q" or "r" or "s" or "t" or "v" or "w" or "x" or "y" or "z":
#     print("Es una consonante")