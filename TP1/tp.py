#Trabajo de python con shreck
#
#⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀ ⣀⣀⣤⣤⣤⣀⡀
#⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀
#⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆
#⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆
#⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆
#⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠸⣼⡿
#⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉
#⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
#⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇
#⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇
#⠀⠀ ⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠇
#⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇
#⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

#Ejercicio 1

base = int(input("Ingresar base del triángulo: "))
altura = int(input("Ingresar altura del triángulo: "))
area = (base*altura)/2
print("El área del triángulo es: ")

#Ejercicio 2

nombre = input("Ingresar nombre: ")
edad = input("Ingresar edad: ")
curso = input("Ingresar curso: ")
carrera = input("Ingresar carrera: ")
print("Mi nombre es "+nombre+" tengo "+edad+" años, estoy en "+curso+" año de "+carrera)
print("Mi nombre es"+nombre+"tengo", edad, "años, estoy en", curso, " año de", carrera)

#Ejercicio 3

numbero1 = int(input("Ingresar número1: "))
numbero2 = int(input("Ingresar número2: "))
resultado = numbero1 + numbero2
print("Resultado ", resultado)

#Ejercicio 4

radio = int(input("Ingresar radio del círculo: "))
pi = 3.14
area = pi*(radio**2)
print("El área es ", area)

#Ejercicio 5

numero1 = int(input("Ingresar número 1: "))
numero2 = int(input("Ingresar número 2: "))
numero3 = int(input("Ingresar número 3: "))
numeros = [numero1, numero2, numero3]
promedio = (numero1+numero2+numero3)/numeros.len()
print("El promedio es", promedio)

#Ejercicio 6

num1 = int(input("Ingresar número 1: "))
num2 = int(input("Ingresar número 2: "))
cajita = num1
num1 = num2
num2 = cajita
print("Numero1: ", num1)
print("Numero2: ", num2)

#Ejercicio 7

numb1 = int(input("Ingresar número 1: "))
numb2 = int(input("Ingresar número 2: "))
print(numb1 + numb2)
print(numb1 - numb2)
print(numb1 * numb2)
print(numb1 / numb2)

#Ejercicio 8

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua", ]
print(asignaturas)

#Ejercicio 9

frutas = ["Manzana", "Banana", "Pera", "Sandía", "Ananá", "Kiwi", "Melón"]
print(frutas)
fruta = int(input("Selecciona el número de opción que quieres elegir"))
print("Tu opción es: ", frutas[fruta+1])
