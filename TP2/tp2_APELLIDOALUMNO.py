#PROFESOR: MAXIMILIANO PERELLÓN
#ALUMNO: EZEQUIEL DUBROWSKY

#           TRABAJO PRACTICO Nº2 - CONDICIONALES

#PARA COMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + C

#PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + U

#Ejercicio 1
edad = int(input("Ingrese su edad: "))
if(edad >= 18):
    print("Mayor de edad")
else:
    print("Acceso denegado (edad insuficiente)")

#Ejercicio 2
pago = int(input("Saldo a pagar: "))
if(pago > 0 and pago <= 100):
    print("Pago en efectivo")
elif(pago <= 300 and pago > 100):
    print("Pago con débito")
elif(pago > 300):
    print("Pago con crédito")

#Ejercicio 3
num1 = int(input("Ingresar primer número: "))
num2 = int(input("Ingresar segundo número: "))
if(num1 != 0 and num2 != 0):
    print(num1 / num2)
else:
    print("Error: no se puede dividir por 0")

#Ejercicio 4
numbero_par = int(input("Ingresar numero: "))
if(numbero_par % 2 == 0):
    print("Es par")
else:
    print("Es impar")

#Ejercicio 5
edad_cliente = int(input("Ingrese su edad: "))
if(edad_cliente < 4):
    print("Pasa gratis")
elif(edad_cliente >= 4 and edad_cliente <= 18):
    print("Paga 200")
elif(edad_cliente > 18):
    print("Paga 500")

#Ejercicio 6
numbero_pos = int(input("Ingresar numero: "))
if(numbero_pos > 0):
    print("positivo")
elif(numbero_pos < 0):
    print("negativo")
else:
    print("cero")

#Ejercicio 7
numb1 = int(input("Ingresar primer número: "))
numb2 = int(input("Ingresar segundo número: "))
numb3 = int(input("Ingresar tercer número: "))
mayor = 0
if(numb1 > numb2 and numb1 > numb3):
    print("El primer número es el mayor")
elif(numb2 > numb1 and numb2 > numb3):
    print("El primer número es el mayor")
elif(numb3 > numb1 and numb3 > numb2):
    print("El primer número es el mayor")

#Ejercicio 8
numbero1 = int(input("Ingresar primer número: "))
numbero2 = int(input("Ingresar segundo número: "))
if(numbero1 % numbero2 == 0):
    print("El primer númeor es múltiplo del segundo")

#Ejercicio 9
number = int(input("Ingresar número del 1 al 7: "))

if(number == 1):
    print("lunes")
elif(number == 2):
    print("martes")
elif(number == 3):
    print("miércoles")
elif(number == 4):
    print("jueves")
elif(number == 5):
    print("viernes")
elif(number == 6):
    print("sábado")
elif(number == 7):
    print("domingo")

#Ejercicio 10
caracter = input("Ingresar un caracter")
vocales = ["a","e","i","o","u"]
if(caracter in vocales):
    print("Es una vocal")
else:
    print("Es una consonante u otra cosa")