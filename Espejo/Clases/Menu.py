import os
# Importa la clase Instrucciones
from Instrucciones import Instrucciones

class Menus:
    def login_menu(self):
        # Limpia la pantalla
        print("\n" * 20)

        # Muestra las opciones disponibles para el usuario
        print("---BIENVENIDO---")
        print("Elija el método de inicio de sesión:")
        print("1. Reconocimiento facial")
        print("2. Contraseña")
        print("3. Salir")

        # Solicita al usuario que ingrese el número de la opción deseada
        numero = input("\nColoque el numero de la opcion(1, 2 o 3): ")

        # Retorna el número de la opción elegida por el usuario
        return numero

    # Función menu para mostrar las opciones al usuario
    def menu(self):
        # Limpia la pantalla
        print("\n" * 20)

        # Muestra las opciones disponibles para el usuario
        print("---INGRESE LO QUE DESEA HACER---")
        print("1. Ver su departamento y municipios junto con su edad")
        print("2. Ver solo su municipio")
        print("3. Cerrar Sesion")

        # Solicita al usuario que ingrese el número de la opción deseada
        deseo = input("\nColoque el numero de la opcion(1, 2 o 3): ")

        # Retorna el número de la opción elegida por el usuario
        return deseo