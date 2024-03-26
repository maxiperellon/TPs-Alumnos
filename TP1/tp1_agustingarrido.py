#PROFESOR: MAXIMILIANO PERELLÓN
#ALUMNO: agustin garrido

#           TRABAJO PRACTICO Nº1

#PARA COMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + C

#PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + U

#Ejercicio 1
#codigo
# Función para calcular el área de un triángulo
# def calcular_area(base, altura):
    # return (base * altura) / 2

# pedir base y altura
#base = float(input("Introduce la base del triángulo: "))
#altura = float(input("Introduce la altura del triángulo: "))

# Calcular area
#area = calcular_area(base, altura)

#resultado
#print("El área del triángulo es: ", area)

#Ejercicio 2
#codigo

#edad= input ("introduce tu edad")
#nombre= input (" tu nombre")
#curso= input ("introduce tu curso")
#carrera= input ("introduce tu carrera")
# Solicitamos al usuario su nombre, edad, curso y carrera
1
# Creamos el mensaje
#mensaje = "Mi nombre es {}, tengo {} años, estoy en {} año de {}.".format(nombre, edad, curso, carrera)

# Imprimimos el mensaje
#print(mensaje)

#
#Ejercicio 3
#codigo
#def calcular_suma(numero1, numero2):
    #return (numero1 + numero2)
#numero1 = int (input("introduce un numero"))
#numero2 = int (input("introduce otro numero"))
#suma = calcular_suma(numero1,numero2)
#print("el resultado de la suma es", suma)

#Ejercicio 4
#codigo
#radio = float(input("introduce el radio"))
#area = 3.14 * (radio ** 2)
#print("El área del círculo es: ", area)

#Ejercicio 5
#codigo
#num1 = int (input ("ingrese el primer numero"))
#num2 = int (input ("ingrese el segundo numero"))
#num3 = int (input ("ingrese el tercer numero"))
#promedio= (num1+num2+num3) /3
#print("el promedio es" ,promedio)

#Ejercicio 6
#codigo
#num1 = int(input("Introduce el primer número entero: "))
#num2 = int(input("Introduce el segundo número entero: "))
#print("Valores originales: num1 =", num1, ", num2 =", num2)
#num1, num2 = num2, num1
#print("Valores intercambiados: num1 =", num1, ", num2 =", num2)

#Ejercicio 7
#codigo

#numero1 = int (input("introduce un numero"))
#numero2 = int (input("introduce otro numero"))
#suma = (numero1 + numero2)
#resta = (numero1 - numero2)
#multiplicacion= (numero1 * numero2)
#division = (numero1/numero2)
#print("el resultado de la suma es", suma)
#print("el resultado de la multiplicacio es", multiplicacion)
#print("el resultado de la division es", division)
#print("el resultado de la resta es", resta)
#Ejercicio 8
#codigo
#asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
#for asignatura in asignaturas:
    #print(asignatura)
#Ejercicio 9
#codigo
    # Definimos una lista de frutas
frutas = ["Manzana", "Banana", "Cereza", "Durazno", "Mango"]

print("Frutas disponibles:")
for i, fruta in enumerate(frutas, start=1):
    print(f"{i}. {fruta}")

num = int(input("Ingresa el número correspondiente a la fruta que deseas: "))

if 1 <= num <= len(frutas):

    print("Has seleccionado: ", frutas[num - 1])
else:
    print("Número inválido. Por favor, intenta de nuevo.")
