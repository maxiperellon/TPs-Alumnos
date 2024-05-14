#PROFESOR: MAXIMILIANO PERELLÓN
#ALUMNO: ....

#           TRABAJO PRACTICO Nº2 - CONDICIONALES

#PARA COMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + C

#PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + U

#Ejercicio 1
#codigo
def mayor_edad():
    edad = int(input("Ingrese su edad: "))
    if edad >= 18:
        print("Usted es mayor de edad.")
    else:
        print("Usted es menor de edad.")
#Ejercicio 2
#codigo
def metodo_pago(gasto):
    if gasto <= 100:
        print("Pago en efectivo.")
    elif gasto > 100 and gasto < 300:
        print("Pago con tarjeta de débito.")
    else:
        print("Pago con tarjeta de crédito.")
#Ejercicio 3
#codigo
def division():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    if num2 != 0:
        print("El resultado de la división es:", num1 / num2)
    else:
        print("Error: No se puede dividir por cero.")
#Ejercicio 4
#codigo
def par_o_impar(numero):
    if numero % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")
#Ejercicio 5
#codigo
def precio_entrada(edad):
    if edad < 4:
        print("Puede entrar gratis.")
    elif edad >= 4 and edad <= 18:
        print("El precio de la entrada es $200.")
    else:
        print("El precio de la entrada es $500.")
#Ejercicio 6
#codigo
def positivo_negativo_cero(numero):
    if numero > 0:
        print("El número es positivo.")
    elif numero < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")
#Ejercicio 7
#codigo
def mayor_de_tres(num1, num2, num3):
    mayor = num1
    if num2 > mayor:
        mayor = num2
    if num3 > mayor:
        mayor = num3
    print("El mayor número es:", mayor)
#Ejercicio 8
#codigo
def es_multiplo(num1, num2):
    if num1 % num2 == 0:
        print("El primer número es múltiplo del segundo.")
    else:
        print("El primer número no es múltiplo del segundo.")
#Ejercicio 9
#codigo
def dia_semana(numero):
    if numero == 1:
        print("Lunes")
    elif numero == 2:
        print("Martes")
    elif numero == 3:
        print("Miércoles")
    elif numero == 4:
        print("Jueves")
    elif numero == 5:
        print("Viernes")
    elif numero == 6:
        print("Sábado")
    elif numero == 7:
        print("Domingo")
    else:
        print("Número inválido.")
#Ejercicio 10
#codigo
def es_vocal_o_consonante(caracter):
    vocales = "aeiouAEIOU"
    if caracter in vocales:
        print("Es una vocal.")
    else:
        print("Es una consonante.")