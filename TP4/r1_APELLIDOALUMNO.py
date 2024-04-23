#PROFESOR: MAXIMILIANO PERELLON
#ALUMNO: EZEQUIEL DUBROWSKY

#           REPASO Nº1 CONDICIONALES - BUCLES

#PARA COMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + C

#PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + U

# #Ejercicio 1
# for i in range(1,11):
#     print(i)

# #Ejercicio 2
# for i in range(2, 21, 2):
#     print(i)

# #Ejercicio 3
# numerocero = int(input("Ingresar número: "))
# if (numerocero == 0):
#     print("es cero")
# elif(numerocero < 0):
#     print("menor a cero")
# elif(numerocero> 0):
#     print("mayor a cero")

# #Ejercicio 4
# for i in range(1,51):
#     if(i % 5 == 0 and i % 3 == 0):
#         print("Cuchau")
#     elif(i % 3 == 0):
#         print("Hola")
#     elif(i % 5 == 0):
#         print("Chau")
#     else:
#         print("Este número no es múltiplo: ", i)

# #Ejercicio 5
# vocal = False
# inputfrase = str(input("Ingrese frase: "))
# for i in inputfrase:
#     if(i == "a"):
#         vocal = True
# if(vocal == True):
#     print("hay letra a")
# else:
#     print("no hay letra a")

# #Ejercicio 6
# vocales = "aeiouAEIOU"
# cuantasvocales = 0
# inputvocales = str(input("Ingresar frase:"))
# for i in inputvocales:
#     if(i in vocales):
#         cuantasvocales += 1
# print(cuantasvocales)

#Ejercicio 7
contra = ""
password = "contraseña"
intentos = 1
while intentos <= 3:
    contraseña = str(input("Ingresar contraseña: "))
    contra = contraseña
    if(contra == password):
        print("Contraseña aceptada")
        break
    if intentos == 3:
        print("Excediste el número de intentos permitidos. Intente de nuevo más tarde.")
        break

    intentos += 1
    

