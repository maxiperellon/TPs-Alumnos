#PROFESOR: MAXIMILIANO PERELLÓN
#ALUMNO: Mazzamati Juan Pablo

#           TRABAJO PRACTICO Nº1

#PARA COMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + C

#PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + U

#Ejercicio 1
#codigo 
base = float(input("Ingresa la longitud de la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))

area = (base * altura) / 2

print("El área del triángulo con base", base, "y altura", altura, "es:", area)


#Ejercicio 2
#codigo

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
curso = input("Ingresa tu curso: ")
carrera = input("Ingresa tu carrera: ")

mensaje = "Mi nombre es {}, tengo {} años, estoy en {} año de {}.".format(nombre, edad, curso, carrera)
print(mensaje)


#Ejercicio 3
#codigo
    
numero1 = int(input("Ingresa el primer número entero: "))
numero2 = int(input("Ingresa el segundo número entero: "))

suma = numero1 + numero2

print("La suma de", numero1, "y", numero2, "es:", suma)


#Ejercicio 4
#codigo
    
radio = float(input("Ingrese el radio del círculo: "))

area = 3.14 * radio ** 2

print("El área del círculo con radio", radio, "es:", area)

#Ejercicio 5
#codigo
    
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))
numero3 = int(input("Ingrese el tercer número entero: "))

promedio = (numero1 + numero2 + numero3) / 3

print("El promedio de", numero1, ",", numero2, "y", numero3, "es:", promedio)


#Ejercicio 6
#codigo

numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))

temp = numero1
numero1 = numero2
numero2 = temp

print("Los números intercambiados son:", numero1, "y", numero2)


#Ejercicio 7
#codigo

numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

if numero2 != 0:
    division = numero1 / numero2
else:
    division = "No se puede dividir por cero"

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)


#Ejercicio 8
#codigo

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

print("Asignaturas del curso:")
for asignatura in asignaturas:
    print(asignatura)

#Ejercicio 9
#codigo

elementos = ["Manzana", "Banana", "Uva", "Naranja", "Pera"]

print("Elementos disponibles:")
for i, elemento in enumerate(elementos, 1):
    print(f"{i}. {elemento}")

opcion = int(input("Ingrese el número correspondiente al elemento deseado: "))

if 1 <= opcion <= len(elementos):
    elemento_seleccionado = elementos[opcion - 1]
    print("El elemento seleccionado es:", elemento_seleccionado)
else:
    print("Opción inválida. Por favor, ingrese un número dentro del rango disponible.")
