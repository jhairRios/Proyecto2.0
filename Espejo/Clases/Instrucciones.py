import os

class Instrucciones:
    def ins_facial():
        print("\n" * 20)

        print("---INSTRUCCIONES---\n")
        print("Para ingresar al sistema, debe permitir el acceso a la cámara. \nSe tomará una foto suya y se comparará con las fotos de los empleados registrados. \nSi la foto coincide con alguna de las fotos registradas, se le permitirá el acceso al sistema. \nSi la foto no coincide con ninguna de las fotos registradas, se le pedirá que la tome nuevamente. \nSi desea salir del sistema, presione X.")
        input("\nPresione Enter para continuar y vea la camara fijamente.")

    def ins_login():
        print("\n" * 20)
        
        print("---INSTRUCCIONES---\n")
        print("Para ingresar al sistema, debe ingresar el usuario y la contraseña correcta. \nSi la contraseña es correcta, se le permitirá el acceso al sistema. \nSi la contraseña es incorrecta, se le pedirá que la ingrese nuevamente. \nSi desea salir del sistema, presione X.")
        input("\nPresione Enter para continuar")

    def ins_menu():
        print("\n" * 20)

        print("---INSTRUCCIONES---\n")
        print("Se muestra un menu con las siguientes opciones: \n\t1. Ver su departamento, municipios y edad. \n\t2. Ver los municipios de su departamento. \n\t3. Salir del sistema. \nIngrese el numero de la opcion que desea. \nSi desea salir del sistema, presione 3.")
        input("\nPresione Enter para continuar")

    def ins_departamentos_edad():
        print("\n" * 20)

        print("---INSTRUCCIONES---\n")
        print("Se le pedirá que ingrese su número de cédula. \nSi la cédula es válida, se le mostrará su departamento y su edad. \nSi la cédula no consta de los 13 digitos, no es válida y se le pedirá que la ingrese nuevamente.")
        input("\nPresione Enter para continuar")

    def ins_municipios():
        print("\n" * 20)

        print("---INSTRUCCIONES---\n")
        print("Se le pedirá que ingrese los primeros 2 digitos de su cédula. \nSi los digitos son válidos, se le mostrarán los municipios de su departamento. \nSi los digitos que ingrese no se encuentran en nuestros registros, se le pedirá que los ingrese nuevamente.")
        input("\nPresione Enter para continuar")