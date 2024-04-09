#PROFESOR: MAXIMILIANO PERELLÓN
#ALUMNO: ....

#           TRABAJO PRACTICO Nº2 - CONDICIONALES

#PARA COMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + C

#PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + U

#Ejercicio 1   
#codigo

# edad = int(input("ingrese su edad"))
# if edad >= 18: 
#     print("sos mayor")
# elif edad < 18:
#     print("sos menor")

#Ejercicio 2
#codigo

# saldo = int(input("ingrese el saldo a pagar"))
# if saldo <= 100:
#     print("paga con efectivo")
# elif saldo > 100 and saldo < 300:
#     print("paga con tarjeta de debito")
# else:
#     print("paga con tarjeta de credito")

#Ejercicio 3
#codigo

# num1 = int(input("ingrese un numero entero"))
# num2 = int(input("ingrese otro numero"))
# if num2!=0:
#     print(num1/num2)
# else:
#     print("error, el segundo numero debe ser distinto de 0")

#Ejercicio 4
#codigo

# numero = int(input("ingrese un numero entero"))
# if numero % 2 == 0: 
#     print("el numero es par")
# else:
#     print("el numero es impar")

#Ejercicio 5
#codigo

# edad = int(input("ingrese su edad"))
# if edad <4:
#     print("Entras gratis")
# elif edad >=4 and edad <=18:
#     print("debes pagar $200")
# elif edad >18:
#     print("deber pagar $500")


#Ejercicio 6
#codigo

# numero = int(input("ingrese un numero"))
# if numero > 0:
#     print("el numero es positivo")
# elif numero < 0:
#     print("el numero es negativo")
# elif  numero == 0:
#     print("el numero es cero")
    
#Ejercicio 7
#codigo

# num1 = int(input("ingrese el primer numero"))
# num2 = int(input("ingrese el segundo numero"))
# num3 = int(input("ingrese el tercer numero"))
# if num1 > num2 and num1 > num3:
#     print ("El mayor es", num1)
# elif num2 > num1 and num2 > num3:
#     print ("El mayor es", num2)
# elif  num3 > num1 and num3 > num2:
#     print ("El mayor es", num3)

#Ejercicio 8
#codigo

# num1 = int(input("ingrese el primer numero"))
# num2 = int(input("ingrese el segundo numero"))
# if num1 % num2 == 0:
#     print("El número", num1, "es múltiplo de", num2)
# else:
#     print("El número", num1, "no es múltiplo de", num2)

#Ejercicio 9
#codigo

# numero = int(input("ingrrese un numero del 1 al 7"))
# if numero == 1:
#     print("lunes")
# elif numero  == 2:
#     print("martes")
# elif numero == 3:
#     print("miércoles")
# elif numero == 4:
#     print("jueves")
# elif numero ==5 :
#     print("viernes")
# elif  numero==6:
#    print("sábado")
# elif  numero==7:
#     print ("domingo")
# else:
#     print("numero incorrecto, por favor ingrese un numero del 1 al 7")


#Ejercicio 10
#codigo

# caracter = str.lower(input("Ingrese una consonante o una vocal"))
# if caracter == "a" or "e" or "i" or "o" or "u":
#     print("el caracter", caracter,  "es una vocal")
# else:
#     print("el caracter", caracter,   "es una consonante")