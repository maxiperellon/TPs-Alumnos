
#PROFESOR: MAXIMILIANO PERELLON
#ALUMNO: ....

#           REPASO Nº1 CONDICIONALES - BUCLES

#PARA COMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + C

#PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + U

#Ejercicio 1
# print("Conteo del 1 al 10: ")
# for num in  range(1,11):
#     print(num)

#Ejercicio 2
# print("El conteo de los números pares del 1 al 20 es: ")
# for  i in range (2, 21, 2):
#     print(i)

# print("El conteo de los numeros pares del 1 al 20 es")
# for i in range (1,20+1):
#     if i % 2 == 0 :
#         print(i)

#Ejercicio 3
# num = int(input("Ingrese un número"))
# if num >= 1:
#     print ("Es positivo")
# elif  num == 0:
#     print ("Es cero")
# else:
#     print ("Es negativo")

#Ejercicio 4
# for i in range (1,50+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("HolaChau :)", i)
#     elif i % 3 == 0:
#         print("Hola :)", i)
#     elif i % 5 == 0:
#         print("Chau :)", i)
#     else:
#         print("Este número no es multiplo", i)
    

#Ejercicio 5
# palabra = str(input("Ingrese una cadena de texto: "))
# for letra in palabra:
#     if letra == "a":
#         print("La letra 'a' se encuentra en el string")

#Ejercicio 6
# palabra = str(input("Ingrese una cadena de texto: "))
# voc=0
# for letra in palabra:
#     if letra in "aeiouAEIOU":
#         # print("La letra 'a' se encuentra en el string")
#         voc+=1
# print("cantidad de vocales: ", voc)

#Ejercicio 7
# password = "contraseña"
# intentos =0
# while intentos < 3:
#     contraseña = input("Ingrese la contraseña: ")
#     if contraseña == password:
#         print("¡Contraseña correcta!")
#         break
#     else:
#         intentos += 1
#         if intentos < 3:
#             print(f"Contraseña incorrecta. Te quedan {3 - intentos} intentos.")
#         else:
#             print("Excediste el número de intentos permitidos. Intente de nuevo más tarde.")