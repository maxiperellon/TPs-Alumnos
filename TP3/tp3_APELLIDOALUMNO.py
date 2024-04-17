#PROFESOR: MAXIMILIANO PERELLON
#ALUMNO: EZEQUIEL DUBROWSKY

#           TRABAJO PRACTICO Nº3 BUCLES

#PARA COMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + C

#PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + U

#Ejercicio 1
for i in range(0,10):
    print(i+1)


#Ejercicio 2
listapromedio = [0,2,3,5,3,1,8,2]
promedio = 0
for i in listapromedio:
    promedio += i
promedio / len(listapromedio)
print(promedio)


#Ejercicio 3
numerowhile = int(input("Ingresar un número: "))
numerito = 0
while numerito < numerowhile:
    if(numerito % 2 == 0):
        print(numerito)
    numerito += 1


#Ejercicio 4
listastr = str(input("Ingresar una frase"))
for i in listastr:
    if(listastr[i] != " "):
        print(listastr[i])


#Ejercicio 5
numeroimpar = int(input("Ingresar un número entero positivo: "))
if(numeroimpar % 2 == 0):
    numbero = 0
    j = 1
    while j <= numeroimpar:
        if(numbero % j != 0):
            numbero += j
        j += 1
    print(numbero)


#Ejercicio 6
numeroimpar2 = int(input("Ingresar un número entero positivo: "))
if(numeroimpar2 % 2 == 0):
    numbero2 = 0
    j2 = 2
    while j2 <= numeroimpar2:
        if(numbero2 % j2 == 0):
            numbero2 += j2
        j2 += 1
    print(numbero2)

#Ejercicio 7
numeroparimpar = int(input("Ingresar números separados por espacios: "))
listaparimpar = numeroparimpar.split()
pares = 0
impares = 0
for i in listaparimpar:
    if(i % 2 == 0):
        pares += 1
    else:
        impares += 1


#Ejercicio 8
tabla = int(input("Ingresar un número: "))
k = 0
numerotabla = 0
while k <= tabla:
    numerotabla = k * tabla
    print(numerotabla)
    k+=1