#PROFESOR: MAXIMILIANO PERELLÓN
#ALUMNO: Luciano Gatica

#           TRABAJO PRACTICO Nº1

#PARA COMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + C

#PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + U

#Ejercicio 1
#base= float(input("Ingrese la base del triángulo"))
#altura= float(input("Ingrese la altura del triángulo"))

#area = (base*altura)/2

#print("area es: ", area)

#Ejercicio 2
#nombre=  (input("solicitar nombre"))
#edad= input("solicitar edad")
#curso= input("solicitar curso")
#carrera= input("solicitar carrera")
#print("Mi nombre es", nombre,"tengo", edad,"años","estoy en",curso,"año de",carrera)



#Ejercicio 3
#númeroentero1= int(input("solicitar número entero1: "))
#númeroentero2= int(input("solicitar número entero2: "))
#r=númeroentero1+númeroentero2
#print(r)


#Ejercicio 4
# import math

# def calcular_area_circulo(radio):
#     area = math.pi * radio**2
#     return area

# def main():
#     try:
#         radio = float(input("Introduce el radio del círculo: "))
#         if radio < 0:
#             print("El radio no puede ser negativo.")
#         else:
#             area = calcular_area_circulo(radio)
#             print("El área del círculo con radio {} es: {:.2f}".format(radio, area))
#     except ValueError:
#         print("Por favor, introduce un número válido para el radio.")

# if __name__ == "__main__":
#     main()

#Ejercicio 5
# def calcular_promedio(num1, num2, num3):
#     promedio = (num1 + num2 + num3) / 3
#     return promedio

# def main():
#     try:
#         num1 = int(input("Introduce el primer número entero: "))
#         num2 = int(input("Introduce el segundo número entero: "))
#         num3 = int(input("Introduce el tercer número entero: "))
        
#         promedio = calcular_promedio(num1, num2, num3)
        
#         print("El promedio de los tres números enteros es:", promedio)
#     except ValueError:
#         print("Por favor, introduce solo números enteros.")

# if __name__ == "__main__":
#     main()

#Ejercicio 6
# def main():
#     try:
#         # Solicitar al usuario que ingrese dos números enteros
#         num1 = int(input("Introduce el primer número entero: "))
#         num2 = int(input("Introduce el segundo número entero: "))

#         # Mostrar los números originales antes del intercambio
#         print("Números originales: num1 =", num1, "y num2 =", num2)

#         # Intercambiar los valores de los números
#         num1, num2 = num2, num1

#         # Mostrar los números intercambiados después del intercambio
#         print("Números intercambiados: num1 =", num1, "y num2 =", num2)
#     except ValueError:
#         print("Por favor, introduce solo números enteros.")

# if __name__ == "__main__":
#     main()

#Ejercicio 7
# def main():
#     try:
#         # Solicitar al usuario que ingrese dos números enteros
#         num1 = int(input("Introduce el primer número entero: "))
#         num2 = int(input("Introduce el segundo número entero: "))

#         # Calcular la suma, resta, multiplicación y división
#         suma = num1 + num2
#         resta = num1 - num2
#         multiplicacion = num1 * num2

#         # Asegurarse de que no se divida entre cero
#         if num2 != 0:
#             division = num1 / num2
#         else:
#             division = "No se puede dividir entre cero."

#         # Mostrar los resultados
#         print("Suma:", suma)
#         print("Resta:", resta)
#         print("Multiplicación:", multiplicacion)
#         print("División:", division)

#     except ValueError:
#         print("Por favor, introduce solo números enteros.")

# if __name__ == "__main__":
#     main()

#Ejercicio 8
# def main():
#     # Definir las asignaturas del curso en una lista
#     asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

#     # Mostrar las asignaturas por pantalla
#     print("Asignaturas del curso:")
#     for asignatura in asignaturas:
#         print(asignatura)

# if __name__ == "__main__":
#     main()

#Ejercicio 9
# def main():
#     # Definir una lista de elementos (frutas en este caso)
#     elementos = ["Manzana", "Banana", "Naranja", "Pera", "Uva"]

#     # Mostrar los elementos disponibles al usuario
#     print("Elementos disponibles:")
#     for i, elemento in enumerate(elementos, start=1):
#         print(f"{i}. {elemento}")

#     try:
#         # Solicitar al usuario ingresar un número correspondiente al elemento deseado
#         seleccion = int(input("Ingrese el número del elemento deseado: "))

#         # Verificar si el número ingresado está dentro del rango válido
#         if 1 <= seleccion <= len(elementos):
#             # Mostrar el elemento seleccionado por pantalla
#             print("Elemento seleccionado:", elementos[seleccion - 1])
#         else:
#             print("Número fuera de rango. Por favor, seleccione un número válido.")
#     except ValueError:
#         print("Por favor, ingrese un número entero válido.")

# if __name__ == "__main__":
#     main()