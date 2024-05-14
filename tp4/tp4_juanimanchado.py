#PROFESOR: MAXIMILIANO PERELLON
#ALUMNO: Manchado Juan Ignacio

#           TRABAJO PRACTICO Nº4 FUNCIONES

#PARA COMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K | CTRL + C

#PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K | CTRL + U

#Ejercicio 1
#codigo
def suma_numeros(num1, num2):
    return num1 + num2
#Ejercicio 2
#codigo
def suma_lista(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma
#Ejercicio 3
#codigo
def ordenar_lista(lista):
    return sorted(lista)
#Ejercicio 4
#codigo
def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for caracter in cadena:
        if caracter in vocales:
            contador += 1
    return contador
#Ejercicio 5
#codigo
def numero_mas_grande(lista):
    return max(lista)
#Ejercicio 6
#codigo
def numeros_pares(lista):
    pares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
    return pares
#Ejercicio 7
#codigo
def buscar_numero(lista, numero):
    return numero in lista

#Ejercicio 8
#codigo
def longitud_cadena(cadena):
    return len(cadena)
#Ejercicio 9
#codigo
import math

def area_circulo(radio):
    return math.pi * radio ** 2

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_cuadrado(lado):
    return lado ** 2