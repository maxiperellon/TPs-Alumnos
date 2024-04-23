#PROFESOR: MAXIMILIANO PERELLON
#ALUMNO: ....

#           REPASO Nº1 CONDICIONALES - BUCLES

#PARA COMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + C

#PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + U

#Ejercicio 1
# for num in range (1, 11):
#     print(num)

#Ejercicio 2
# for x in range(2,21,2):
#     print(x)

#Ejercicio 3
# num=int(input("Ingrese un numero: "))
# if num > 0:
#     print("El numero es positivo")  
# elif num < 0:
#        print("El numero es negativo")
# else:
#       print("El numero es cero")

# #Ejercicio 4
# for x in range (1,51):    
#     if x % 3 == 0 and x % 5 == 0:
#         print("HolaChau",x)
#     elif x % 3 == 0:
#         print("Hola", x)
#     elif x % 5 == 0:
#         print("Chau", x)

#Ejercicio 5
# cadena=input("ingrese una cadena de texto: ")
# if "a" in cadena or "A":
#     print("La cadena es contiene una cadena")

#Ejercicio 6
# cadena=str(input("ingrese una cadena de texto: "))
# vocales=0
# for letra in cadena:
#     if letra in "aeiouAEIOU":
#         vocales+=1
# print("la cantidad de vocales en ", cadena,  "es: ", vocales)

#Ejercicio 7
password ="contraseña"
intentos =0 
while intentos <3:
    contrasena=input("Ingrese su contraseña: ")
    if contrasena == password:
        print("Bienvenido")
        break
    else:
        print("Contraseña incorrecta")
        intentos+=1
    if intentos == 3:
        print("numero de intentos exedidos")