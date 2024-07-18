import TotalDepartamentos
import os

from Menu import Menus
from Login import Login
from Instrucciones import Instrucciones

# clase de opciones del programa
class opcionesMenu:

    # limpiar pantalla
    def limpiar_pantalla(self):
         print("\n" * 20)

    
    # mostrar departamento y edad
    def mostrar_depto_edad(self):
        menus = Menus()
        self.limpiar_pantalla()

        print("---VER SU DEPARTAMENTO, MUNICIPIOS Y EDAD---\n")

        
        cedula = input("Ingrese su número de cédula: ")

        if len(cedula) == 13:
            
            ano = int(cedula[4:8])
            departamento = str(cedula[0:4])
            edad = 2024 - ano

            if departamento in TotalDepartamentos.Departamentos:
                
                if ano >= 1924 and ano <= 2024:
                    print("Su departamento es:", TotalDepartamentos.Departamentos[departamento], "\nSu edad es:", edad)

                    input("\nPresione Enter para volver al menu principal")

                    n = menus.menu()
                    self.opcion(n)
                else:
                    input("\nEl año de su cedula no se admite, solo años entre 1924 y 2024, intente de nuevo presionando Enter.")
                    self.mostrar_depto_edad()

            else:
                input("\nDepartamento no valido, intente de nuevo presionando Enter.")
                self.mostrar_depto_edad()

        else:
             input("\nCedula no valida, intente de nuevo presionando Enter.")
             self.mostrar_depto_edad()


    # mostrar municipios segun cedula
    def mostrar_municipios_cedula(self):
        menus = Menus()
        self.limpiar_pantalla()

        print("---VER LOS MUNICIPIOS DE SU DEPARTAMENTO---\n")

        cedula = input("Ingrese los primeros 2 digitos de su cedula: ")
        municipio = str(cedula[0:2])
        
        if municipio == "01":
            print("\nLos municipios de su departamento son:")
            for clave, valor in TotalDepartamentos.Atlantida.items():
                print(clave, valor)
        elif municipio == "02":
            print("\nLos municipios de su departamento son:")
            for clave, valor in TotalDepartamentos.Colon.items():
                print(clave, valor)
        elif municipio == "03":
            print("\nLos municipios de su departamento son:")
            for clave, valor in TotalDepartamentos.Comayagua.items():
                print(clave, valor)        
        elif municipio == "04":
            print("\nLos municipios de su departamento son:")
            for clave, valor in TotalDepartamentos.Copan.items():
                print(clave, valor)
        elif municipio == "05":
            print("\nLos municipios de su departamento son:")
            for clave, valor in TotalDepartamentos.Cortes.items():
                print(clave, valor)
        elif municipio == "06":
            print("\nLos municipios de su departamento son:")
            for clave, valor in TotalDepartamentos.Choluteca.items():
                print(clave, valor)
        elif municipio == "07":
            print("\nLos municipios de su departamento son:")
            for clave, valor in TotalDepartamentos.Paraiso.items():
                print(clave, valor)
        elif municipio == "08":
            print("\nLos municipios de su departamento son:")
            for clave, valor in TotalDepartamentos.Morazan.items():
                print(clave, valor)
        elif municipio == "09":
            print("\nLos municipios de su departamento son:")
            for clave, valor in TotalDepartamentos.Gracias.items():
                print(clave, valor)
        elif municipio == "10":
            print("\nLos municipios de su departamento son:")
            for clave, valor in TotalDepartamentos.Intibuca.items():
                print(clave, valor)
        elif municipio == "11":
            print("\nLos municipios de su departamento son:")
            for clave, valor in TotalDepartamentos.Isla.items():
                print(clave, valor)
        elif municipio == "12":
            print("\nLos municipios de su departamento son:")
            for clave, valor in TotalDepartamentos.Paz.items():
                print(clave, valor)
        elif municipio == "13":
            print("\nLos municipios de su departamento son:")
            for clave, valor in TotalDepartamentos.Lempira.items():
                print(clave, valor)
        elif municipio == "14":
            print("\nLos municipios de su departamento son:")
            for clave, valor in TotalDepartamentos.Ocotepeque.items():
                print(clave, valor)
        elif municipio == "15":
            print("\nLos municipios de su departamento son:")
            for clave, valor in TotalDepartamentos.Olancho.items():
                print(clave, valor)
        elif municipio == "16":
            print("\nLos municipios de su departamento son:")
            for clave, valor in TotalDepartamentos.Santa.items():
                print(clave, valor)
        elif municipio == "17":
            print("\nLos municipios de su departamento son:")
            for clave, valor in TotalDepartamentos.Valle.items():
                print(clave, valor)
        elif municipio == "18":
            print("\nLos municipios de su departamento son:")
            for clave, valor in TotalDepartamentos.Yoro.items():
                print(clave, valor)
        else:
            input("\nLos digitos ingresados no corresponden a ningun departamento, intente de nuevo presionando Enter.")
            self.mostrar_municipios_cedula()
                    
        input("\nPresione Enter para volver al menu principal")
        n = menus.menu()
        self.opcion(n)

    # definir decision del menu
    def opcion(self, opcion):
        menus = Menus()
        login = Login()

        if opcion == "1":
            Instrucciones.ins_departamentos_edad()
            self.mostrar_depto_edad()

        elif opcion == "2":
            Instrucciones.ins_municipios()
            self.mostrar_municipios_cedula()

        elif opcion == "3":
            m = menus.login_menu()
            login.elegir_metodo(m)
            n = menus.menu()
            self.opcion(n)

        else:
            input("\nOpcion no valida, presione Enter para intentar de nuevo.")
            n = menus.menu()
            self.opcion(n)    