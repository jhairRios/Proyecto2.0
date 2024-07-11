import os
import sys
sys.path.append('C:\\Users\\jorge\\Desktop\\Inicio\\UTH\\2024\\2-2024\\AVANZADA_II\\II_P\\Proyecto\\Clases')
os.system('cls'if os.name == 'nt' else 'clear')

from Clases.Login import verificar_acceso 
from Clases.Menu import menu
from Clases.Opciones import opcionesMenu

booleana = verificar_acceso()

if booleana == True:
    n = menu()
    opciones = opcionesMenu()
    opciones.opcion(n)
    