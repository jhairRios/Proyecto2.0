import TotalDepartamentos
import os

from Menu import menu

# clase de opciones del programa
class opcionesMenu:

    # limpiar pantalla
    def limpiar_pantalla(self):
         os.system('cls' if os.name == 'nt' else 'clear')

    
    # mostrar departamento y edad
    def mostrar_depto_edad(self):

        self.limpiar_pantalla()

        print("---VER SU DEPARTAMENTO, MUNICIPIOS Y EDAD---\n")

        print("Ingrese su número de cédula")
        cedula = input()

        if len(cedula) == 13:
            
            ano = int(cedula[4:8])
            departamento = str(cedula[0:4])
            edad = 2024 - ano

            if departamento in TotalDepartamentos.Departamentos:
                
                if ano >= 1924 and ano <= 2024:
                    print("Su departamento es:", TotalDepartamentos.Departamentos[departamento], "\nSu edad es:", edad)

                    input("\nPresione Enter para volver al menu principal")

                    n = menu()
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
        
        self.limpiar_pantalla()

        print("Ingrese su numero de cedula")
        cedula = input()
        municipio = str(cedula[0:2])
        print("Los municipios de su departamento son:")
        if municipio == "01":
            for clave, valor in TotalDepartamentos.Atlantida.items():
                print(clave, valor)
        elif municipio == "02":
                for clave, valor in TotalDepartamentos.Colon.items():
                    print(clave, valor)
        elif municipio == "03":
                for clave, valor in TotalDepartamentos.Comayagua.items():
                    print(clave, valor)        
        elif municipio == "04":
                for clave, valor in TotalDepartamentos.Copan.items():
                    print(clave, valor)
        elif municipio == "05":
                for clave, valor in TotalDepartamentos.Cortes.items():
                    print(clave, valor)
        elif municipio == "06":
                for clave, valor in TotalDepartamentos.Choluteca.items():
                    print(clave, valor)
        elif municipio == "07":
                for clave, valor in TotalDepartamentos.Paraiso.items():
                    print(clave, valor)
        elif municipio == "08":
                for clave, valor in TotalDepartamentos.Morazan.items():
                    print(clave, valor)
        elif municipio == "09":
                for clave, valor in TotalDepartamentos.Gracias.items():
                    print(clave, valor)
        elif municipio == "10":
                for clave, valor in TotalDepartamentos.Intibuca.items():
                    print(clave, valor)
        elif municipio == "11":
                for clave, valor in TotalDepartamentos.Isla.items():
                    print(clave, valor)
        elif municipio == "12":
                for clave, valor in TotalDepartamentos.Paz.items():
                    print(clave, valor)
        elif municipio == "13":
                for clave, valor in TotalDepartamentos.Lempira.items():
                    print(clave, valor)
        elif municipio == "14":
                for clave, valor in TotalDepartamentos.Ocotepeque.items():
                    print(clave, valor)
        elif municipio == "15":
                for clave, valor in TotalDepartamentos.Olancho.items():
                    print(clave, valor)
        elif municipio == "16":
                for clave, valor in TotalDepartamentos.Santa.items():
                    print(clave, valor)
        elif municipio == "17":
                for clave, valor in TotalDepartamentos.Valle.items():
                    print(clave, valor)
        elif municipio == "18":
                for clave, valor in TotalDepartamentos.Yoro.items():
                    print(clave, valor)


    # definir decision del menu
    def opcion(self, opcion):
        if opcion == 1:
            self.mostrar_depto_edad()
        elif opcion == 2:
            self.mostrar_municipios_cedula()
        elif opcion == 3:
            print("Hasta luego")
            exit()
        else:
            input("\nOpcion no valida, presione Enter para intentar de nuevo.")

            n = menu()
            self.opcion(n)


    