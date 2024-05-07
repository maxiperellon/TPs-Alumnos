#PROFESOR: MAXIMILIANO PERELLON
#ALUMNO: EZEQUIEL DUBROWSKY

#           TRABAJO PRACTICO Nº4 FUNCIONES

#PARA COMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K | CTRL + C

#PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K | CTRL + U

#Ejercicio 1
def sumar(num1, num2):
    return num1 + num2

#Ejercicio 2
def sumalista(lista):
    total = 0
    for i in lista:
        total += i
    return total

#Ejercicio 3
def ordenalista(lista):
    lista.sort()
    return lista

#Ejercicio 4
def cuentavocales(cadena):
    vocales = "aeiouAEIOU"
    total = 0
    for i in cadena:
        if i in vocales:
            i += 1
    return total

#Ejercicio 5
def maximolista(lista):
    maximo = max(lista)
    return maximo

#Ejercicio 6
def buscapares(lista):
    pares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)


#Ejercicio 7
def buscanumeros(lista, numero):
    haynumero = False
    if numero in lista:
        haynumero = True
    return haynumero

#Ejercicio 8
def longitud(cadena):
    longitud = len(cadena)
    return longitud

#Ejercicio 9
def areacuadrado(lado):
    area = lado ** 2

def areacuadrado(base, altura):
    area = (base * altura) / 2
    
def areacuadrado(radio):
    pi = 3.141592
    area = radio * pi