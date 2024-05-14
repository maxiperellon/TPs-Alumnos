# #PROFESOR: MAXIMILIANO PERELLON
# #ALUMNO: Chiara Matarazzo
# #           TRABAJO PRACTICO Nº4 FUNCIONES

# #PARA COMENTAR UN BLOQUE DE CODIGO: 
# ##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K | CTRL + C

# #PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
# ##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K | CTRL + U

# #Ejercicio 1
# def suma_numeros(num1, num2):
#     return num1 + num2

# #Ejercicio 2
# def suma_lista(lista):
#     suma = 0
#     for num in lista:
#         suma += num
#     return suma

# #Ejercicio 3
# def ordenar_lista(lista):
#     return sorted(lista)

# #Ejercicio 4
# def contar_vocales(cadena):
#     vocales = 'aeiou'
#     contador = 0
#     for c in cadena.lower():
#         if c in vocales:
#             contador += 1
#     return contador

# #Ejercicio 5
# def mayor_numero(lista):
#     mayor = lista[0]
#     for num in lista:
#         if num > mayor:
#             mayor = num
#     return mayor

# #Ejercicio 6
# def numeros_pares(lista):
#     lista_pares = []
#     for num in lista:
#         if num % 2 == 0:
#             lista_pares.append(num)
#     return lista_pares

# #Ejercicio 7
# def esta_en_lista(lista, num):
#     for elemento in lista:
#         if elemento == num:
#             return True
#     return False

# #Ejercicio 8
# def longitud_cadena(cadena):
#     contador = 0
#     for c in cadena:
#         contador += 1
#     return contador

# #Ejercicio 9
# def area_circulo(radio):
#     pi = 3.14
#     area = pi * radio ** 2
#     return area

# def area_triangulo(base, altura):
#     return (base * altura) / 2

# def area_cuadrado(lado):
#     return lado ** 2