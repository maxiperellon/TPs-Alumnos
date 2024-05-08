#PROFESOR: MAXIMILIANO PERELLON
#ALUMNO: TADEO GIORDANO

#           TRABAJO PRACTICO Nº4 FUNCIONES

#PARA COMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K | CTRL + C

#PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K | CTRL + U

#Ejercicio 1
# def suma (num1, num2):
#     suma = num1 + num2
#     return suma
# print(suma(5,3))

#Ejercicio 2
# def suma_lista(lista):
#     suma = 0
#     for elemento in lista:
#         suma += elemento
#     return suma
# lista = [1, 2, 3, 4, 5]
# resultado = suma_lista(lista)
# print("La suma de los elementos de la lista es:", resultado)

#Ejercicio 3
# def ordenar_lista(lista):
#     lista = sorted(lista)
#     return lista
# lista = [5, 2, 3, 1, 4]
# lista = ordenar_lista(lista)
# print("La lista ordenada es:", lista)

#Ejercicio 4
# def contar_vocales(string):
#     contador_vocales = 0
#     vocales_validas = "aeiou"
#     for letra in string:
#         if letra in vocales_validas:
#             contador_vocales += 1
#     return contador_vocales
# string = "mi nombre es tadeo"
# resultado = contar_vocales(string)
# print("La cantidad de vocales en la cadena es:", resultado)

#Ejercicio 5
#def numero_mas_grande(lista):
#     maximo = lista[0]
#     for numero in lista:
#         if numero > maximo:
#             maximo = numero
#     return maximo
# lista = [1, 2, 3, 4, 5]
# resultado = numero_mas_grande(lista)
# print("El número más grande de la lista es:", resultado)

#Ejercicio 6
# def numero_par(lista):
#    pares = []
#    for numero in lista:
#        if numero % 2 ==  0:
#            pares.append(numero)
#    return pares
# nums = [5,3,4,7,9,2,1,6,10,8]
# resultados = numero_par(nums)
# print ("Los numeros pares son: ",resultados)

#Ejercicio 7
# def buscar_numero(lista, numero):
#     if numero in lista:
#         return True
#     else:
#         return False

# lista = [1, 2, 3, 4, 5]
# numero = 5
# resultado = buscar_numero(lista, numero)
# print("El número está en la lista:", resultado)

#Ejercicio 8
# def longitud_string(string):
#     longitud = 0
#     for letra in string:
#         longitud += 1
#     return longitud

# string = "hola que tal"
# print("La longitud del string es: ", longitud_string(string))

#Ejercicio 9
# Función para calcular el área de un círculo
# def area_circulo(radio):
#     pi = 3.14
#     area = pi * radio**2
#     return area

# # Función para calcular el área de un triángulo
# def area_triangulo(base, altura):
#     area = (base * altura) / 2
#     return area

# # Función para calcular el área de un cuadrado
# def area_cuadrado(lado):
#     area = lado**2
#     return area