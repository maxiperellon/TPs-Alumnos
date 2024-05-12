#PROFESOR: MAXIMILIANO PERELLON
#ALUMNO: AUGUSTO ALVAREZ

#           TRABAJO PRACTICO Nº4 FUNCIONES

#PARA COMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K | CTRL + C

#PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K | CTRL + U

#Ejercicio 1
#codigo

# def suma (n1,n2):
#     sum= n1 + n2
#     return sum
# print(suma(5,3))



#Ejercicio 2
#codigo

# def suma_lista(lista):
#     return sum(lista)
# print(suma_lista([9,8,7,6]))

#Ejercicio 3
#codigo

# def ordenar_lista(lista):
#     return sorted(lista)
# print(ordenar_lista([5,4,3,2,1])) 

#Ejercicio 4
#codigo

# def contar_vocales(cadena):
#     vocales = 'aeiouAEIOUáéíóúÁÉÍÓÚ'
#     conteo = 0
#     for letra in cadena:
#         if letra in vocales:
#             conteo += 1
#     return conteo
# print(contar_vocales("Hola, ¿cómo estás?"))

#Ejercicio 5
#codigo

# def encontrar_mayor(lista_numeros):
#     mayor = lista_numeros[0]
#     for num in lista_numeros:
#         if num > mayor:
#             mayor = num
#     return mayor
# print(encontrar_mayor([10,56,23,120,94]))

#Ejercicio 6
#codigo

# def obtener_pares(lista_numeros):
#     pares = []
#     for num in lista_numeros:
#         if num % 2 == 0:
#             pares = pares + [num]
#     return pares
# print(obtener_pares([10,56,23,120,94,11,17]))

#Ejercicio 7
#codigo

# def esta_en_lista(lista, numero):
#     if numero in lista:
#         return True
#     else:
#         return False
# mi_lista = [1, 2, 3, 4, 5]
# mi_numero = 10
# print(esta_en_lista(mi_lista, mi_numero)) 

#Ejercicio 8
#codigo

# def obtener_longitud(texto):
#     return len(texto)
# print(obtener_longitud("Hola"))

#Ejercicio 9
#codigo circulo

# def calcular_area_circulo(radio):
#     pi = 3.141592653589793
#     area = pi * (radio ** 2)
#     return area
# radio = 5.0
# area = calcular_area_circulo(radio)
# print("El área del círculo con radio", radio, "es: ", area)

#codigo triangulo
# def calcular_area_triangulo(base, altura):
#     area = (base * altura) / 2
#     return area
# base = 10.0
# altura = 5.0
# area = calcular_area_triangulo(base, altura)
# print("El área del triángulo con base", base, "y altura", altura, "es: ", area)

#codigo cuadrado
# def calcular_area_cuadrado(lado):
#     area = lado * lado
#     return area
# lado = 4.0
# area = calcular_area_cuadrado(lado)
# print("El área del cuadrado con lado", lado, "es: ", area)


