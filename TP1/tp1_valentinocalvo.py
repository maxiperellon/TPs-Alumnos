# #PROFESOR: MAXIMILIANO PERELLÓN
# #ALUMNO: Luciano Gatica

# #           TRABAJO PRACTICO Nº1

# #PARA COMENTAR UN BLOQUE DE CODIGO: 
# ##SELECCIONAR EL CODIGO QUE QUERES COMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + C

# #PARA DESCOMENTAR UN BLOQUE DE CODIGO: 
# ##SELECCIONAR EL CODIGO QUE QUERES DESCOMENTAR E INGRESAR LOS ATAJOS DE TECLADO: CTRL + K / CTRL + U

# #Ejercicio 1
# # x_b= float(input("Ingrese la base del triángulo"))
# # x_a= float(input("Ingrese laaltura del triángulo"))

# # area = (x_b*x_a)/2

# # print("area es: ", area)

# # Ejercicio 2
# invocador = input("Nombre de invocador: ")
# nivel = input("Nivel de invocador: ")
# rol = input("Rol principal: ")
# campeon = input("Campeón favorito: ")
# print("Invocador:", invocador, "Nivel:", nivel, "Rol:", rol, "Campeón favorito:", campeon)

# # Ejercicio 3
# daño1 = int(input("Daño de habilidad 1: "))
# daño2 = int(input("Daño de habilidad 2: "))
# daño_total = daño1 + daño2
# print("Daño total:", daño_total)

# # Ejercicio 4
# import math

# def calcular_area_terreno(radio):
#     area = math.pi * radio**2
#     return area

# def main():
#     try:
#         radio = float(input("Tamaño del terreno (radio): "))
#         if radio < 0:
#             print("El tamaño del terreno no puede ser negativo.")
#         else:
#             area = calcular_area_terreno(radio)
#             print("El área del terreno es: {:.2f}".format(area))
#     except ValueError:
#         print("Por favor, introduce un número válido para el tamaño del terreno.")

# if __name__ == "__main__":
#     main()

# # Ejercicio 5
# def calcular_promedio_kda(kills, deaths, assists):
#     promedio = (kills + assists) / deaths
#     return promedio

# def main():
#     try:
#         kills = int(input("Kills: "))
#         deaths = int(input("Deaths: "))
#         assists = int(input("Assists: "))
        
#         promedio_kda = calcular_promedio_kda(kills, deaths, assists)
        
#         print("Promedio KDA:", promedio_kda)
#     except ValueError:
#         print("Por favor, introduce solo números enteros.")

# if __name__ == "__main__":
#     main()

# # Ejercicio 6
# def main():
#     try:
#         oro_equipo1 = int(input("Oro equipo 1: "))
#         oro_equipo2 = int(input("Oro equipo 2: "))

#         print("Oro inicial: Equipo 1 =", oro_equipo1, "Equipo 2 =", oro_equipo2)

#         oro_equipo1, oro_equipo2 = oro_equipo2, oro_equipo1

#         print("Oro intercambiado: Equipo 1 =", oro_equipo1, "Equipo 2 =", oro_equipo2)
#     except ValueError:
#         print("Por favor, introduce solo números enteros.")

# if __name__ == "__main__":
#     main()

# # Ejercicio 7
# def main():
#     try:
#         asesinatos_equipo1 = int(input("Asesinatos equipo 1: "))
#         asesinatos_equipo2 = int(input("Asesinatos equipo 2: "))

#         asesinatos_totales = asesinatos_equipo1 + asesinatos_equipo2

#         print("Asesinatos totales:", asesinatos_totales)
#     except ValueError:
#         print("Por favor, introduce solo números enteros.")

# if __name__ == "__main__":
#     main()

# # Ejercicio 8
# def main():
#     campeones = ["Garen", "Lux", "Ahri", "Ezreal", "Jinx"]

#     print("Campeones disponibles:")
#     for campeon in campeones:
#         print(campeon)

# if __name__ == "__main__":
#     main()

# # Ejercicio 9
# def main():
#     objetos = ["Daga", "Espada", "Arco", "Cetro", "Guantelete"]

#     print("Objetos disponibles:")
#     for i, objeto in enumerate(objetos, start=1):
#         print(f"{i}. {objeto}")

#     try:
#         seleccion = int(input("Selecciona el número del objeto deseado: "))

#         if 1 <= seleccion <= len(objetos):
#             print("Objeto seleccionado:", objetos[seleccion - 1])
#         else:
#             print("Número fuera de rango. Por favor, selecciona un número válido.")
#     except ValueError:
#         print("Por favor, introduce un número entero válido.")

# if __name__ == "__main__":
#     main()
