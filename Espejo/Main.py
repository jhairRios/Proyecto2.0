import os
import sys
sys.path.append('C:\\Users\\jorge\\Desktop\\Inicio\\UTH\\2024\\2-2024\\AVANZADA_II\\II_P\\ControladorReconocimientoFacial\\.venv\\Clases')

from Clases.Login import Login
from Clases.Menu import Menus
from Clases.Opciones import opcionesMenu

menus = Menus()
login = Login()

m = menus.login_menu()
booleana = False
booleana = login.elegir_metodo(m)
print(booleana)

if booleana == True or booleana == None:
    n = menus.menu()
    opciones = opcionesMenu()
    opciones.opcion(n)
