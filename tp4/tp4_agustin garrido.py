#PROFESOR: MAXIMILIANO PERELLON
#ALUMNO: agustin garrido

#           TRABAJO PRACTICO Nº4 FUNCIONES

#PARA COMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K | CTRL + C

#PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K | CTRL + U

#Ejercicio 1
#codigo
#def suma(a, b):

#    return a + b


#resultado = suma(5, 3)
#print(f"La suma es: {resultado}")

#Ejercicio 2
#codigo
#def suma_lista(lista):

#    suma_total = 0
 #   for elemento in lista:
#        suma_total += elemento
#    return suma_total


#mi_lista = [1, 2, 3, 4, 5]
#resultado = suma_lista(mi_lista)
#print(f"La suma de los elementos de la lista es: {resultado}")

#Ejercicio 3
#codigo
#def ordenar_lista(lista):
 #   lista.sort()
#    return lista
#def ordenar_lista(lista):
#    return sorted(lista)
#Ejercicio 4
#codigo
#def count_vowels(cadena):
#    vowels = 'aeiouAEIOU'
#    count = 0
#    for char in cadena:
#        if char in vowels:
#            count += 1
#    return count
#Ejercicio 5
#codigo
#def numero_mayor(lista):
    
 #   max_numero = lista[0]

 #   for numero in lista:
 #       if numero > max_numero:
#            max_numero = numero

#    return max_numero

#numeros = [2, 13, 40, 9]
#resultado = numero_mayor(numeros)
#print(f"El número más grande de la lista es: {resultado}")

#Ejercicio 6
#codigo
#def numeros_pares(lista):
   
#    pares = []

#    for numero in lista:
#        if numero % 2 == 0:
#            pares.append(numero)  

#    return pares


#numeros = [2, 13, 40, 9, 6, 17]
#pares_resultado = numeros_pares(numeros)
#print(f"Los números pares son: {pares_resultado}")

#Ejercicio 7
#codigo
#def esta_en_lista(lista, numero):
#    return numero in lista

#numeros = [2, 13, 40, 9]
#numero_buscar = 13
#resultado = esta_en_lista(numeros, numero_buscar)
#print(f"¿El número {numero_buscar} está en la lista? {resultado}")

#Ejercicio 8
#codigo
#def longitud_cadena(texto):
#    return len(texto)

#cadena = "Hola, tú"
#resultado = longitud_cadena(cadena)
#print(f"La longitud de la cadena es: {resultado}")

#Ejercicio 9
#codigo
#import math

#def area_circulo(radio):
    #"""
#    Calcula el área de un círculo dado su radio.
    #"""
#    return math.pi * (radio ** 2)
#
#radio_circulo = 5
#area_del_circulo = area_circulo(radio_circulo)
#print(f"El área del círculo con radio {radio_circulo} es: {area_del_circulo:.2f}")


#def area_triangulo(base, altura):
    #"""
#    Calcula el área de un triángulo dado su base y altura.
    #"""
#    return 0.5 * base * altura

#base_triangulo = 8
#altura_triangulo = 6
#area_del_triangulo = area_triangulo(base_triangulo, altura_triangulo)
#print(f"El área del triángulo con base {base_triangulo} y altura {altura_triangulo} es: {area_del_triangulo:.2f}")


#def area_cuadrado(lado):
#    """
#    Calcula el área de un cuadrado dado su lado.
#    """
#    return lado ** 2

#lado_cuadrado = 4
#area_del_cuadrado = area_cuadrado(lado_cuadrado)
#print(f"El área del cuadrado con lado {lado_cuadrado} es: {area_del_cuadrado:.2f}")
