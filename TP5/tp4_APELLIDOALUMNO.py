#PROFESOR: MAXIMILIANO PERELLON
#ALUMNO: ....

#           TRABAJO PRACTICO Nº4 FUNCIONES

#PARA COMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K | CTRL + C

#PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K | CTRL + U

#Ejercicio 1
# def suma (p1, p2):
#     suma = p1 + p2
#     return suma

# print(suma(15,15))



#Ejercicio 2
# lista=[1,2,3,4,5]
# def lista_suma (lista):
#     suma = 0
#     for i in lista:
#         suma = suma + i
#     return suma

# print(lista_suma(lista))

#Ejercicio 3

# def ordenar_lista(lista):
#     return sorted(lista)

# lista = [5, 6, 3, 12, 9]
# lista_ordenada = ordenar_lista(lista)
# print(lista_ordenada)

#Ejercicio 4
# cadena="Cadena de caracteres"
# def cadenacara (cadena):
#     vocales=0
#     for i in cadena:
#         if i in "aeiouAEIOU":
#             vocales = vocales + 1
#     return vocales
# print(cadenacara(cadena))
    

#Ejercicio 5
#codigo

#Ejercicio 6
# lista=[10,15,16,28,30,33,37,40]
# def lista_suma (lista):
#  pares = [num for num in lista if num % 2 == 0]
#  return pares
# print(lista_suma(lista))


#Ejercicio 7

# lista = [7, 4, 2, 1]
# numero = int(input("Ingrese un digito: "))

# def lista_numero(lista, numero):
#     for i in lista:
#         if i == int(numero):  
#             return True  
#     return False  

# print(lista_numero(lista, numero))

#Ejercicio 8
# def longitud_cadena(cadena):
#     return len(cadena)

# cadena = input("Ingrese una cadena de texto: ")
# longitud = longitud_cadena(cadena)
# print("La longitud de la cadena es:", longitud)

#Ejercicio 9
# def area_circulo(parametro):
#     return 3.14159 * parametro * parametro
# parametro = int(input("ingrese el radio del circulo: "))
# area = area_circulo(parametro)
# print("El area del circulo es:", area)

# def area_triangulo(parametros):
#     return  parametros / 2
# base = int(input("ingrese la base del triangulo: "))
# altura = int(input("ingrese la altura del triangulo: "))
# parametros=base*altura
# area=area_triangulo(parametros)
# print("El area del triangulo es:", area)

# Función para calcular el área de un cuadrado
# def area_cuadrado(parametro):
#     return parametro * parametro
# parametro=int(input("Ingrese el lado del cuadrado: "))
# area=area_cuadrado(parametro)
# print("El area del cuadrado es: ", area)