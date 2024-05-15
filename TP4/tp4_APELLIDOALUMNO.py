#PROFESOR: MAXIMILIANO PERELLON
#ALUMNO: ....

#           TRABAJO PRACTICO Nº4 FUNCIONES

#PARA COMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K | CTRL + C

#PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K | CTRL + U

#Ejercicio 1
#codigo

# def suma_numeros(num1, num2):
#     return num1 + num2

# suma_numeros(2,1)
# print(suma_numeros(2,1))

#Ejercicio 2
#codigo

# def suma_lista(lista):
#     sum = 0
#     for i in lista:
#         sum = sum + i
#     return sum 

# lista1 = [1, 2 ,3]

# suma_lista(lista1)
# print(suma_lista(lista1))

#Ejercicio 3
#codigo

# def ordenar_lista(lista):
#     return sorted(lista)

# lista1 = [5,9,3,1,2,0]
# print(ordenar_lista(lista1))

#Ejercicio 4
#codigo

# def cantidad_vocales(cadena):
#     sum = 0
#     for i in cadena:
#         if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i =="A" or i == "E" or i == "I" or i == "O" or i == "U":
#             sum = sum + 1
#         else:
#             sum = sum
#     return sum
# print(cantidad_vocales("Eres un magnet"))

#Ejercicio 5
#codigo
# lista1 = [4, 3, 7, 9, 0]
# def number_higher(lista_de_numeros):
#     max = lista_de_numeros[0]
#     for i in lista_de_numeros:
#         if i >= max:
#             max = i
#         else:
#             max = max
#     return max 
# print(number_higher(lista1))

#Ejercicio 6
#codigo

# def numeros_pares(lista_de_numeros):
#     lista = []
#     for i in lista_de_numeros:
#         if i % 2 == 0:
#             lista.append(i)
#         else:
#             lista = lista
#     return lista
# lista1 = [3, 8, 9, 16, 33, 12, 54, 55, 99, 100]
# print(numeros_pares(lista1))
            
#Ejercicio 7
#codigo

# def true_false(lista,numero):
#     for i in lista:
#         if i == numero:
#             return True
#     return False
# numero1 = 8
# lista1 = [2, 6, 8, 1, 3, 0, 9,]
# print(true_false(lista1, numero1))

#Ejercicio 8
#codigo

# def longitud(cadena_de_texto):
#     return len(cadena_de_texto)

# print(longitud("Hola mundo"))

#Ejercicio 9
#codigo

# def area_circulo(radio):
#     pi = 3.14
#     radio_cuadrado = radio**2
#     return pi*radio_cuadrado

# print(area_circulo(10))

# def area_triangulo(base, altura):
#     return (base * altura)/2

# print(area_triangulo(10,20))

# def area_cuadrado(base, altura):
#     return (base * altura)

# print(area_cuadrado(10,20))
