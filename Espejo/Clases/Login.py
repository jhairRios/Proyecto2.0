import os
import cv2
import face_recognition
import face_recognition as fr
import numpy

# Importa la clase Instrucciones
from Instrucciones import Instrucciones
from Menu import Menus

class Login:

    def facial(self):
        ruta = "C:\\Users\\jorge\\Desktop\\Inicio\\UTH\\2024\\2-2024\\AVANZADA_II\\II_P\\ControladorReconocimientoFacial\\.venv\\Clases\\Empleados"  # Carpeta donde se encuentran las fotos de los empleados

        # Muestra las instrucciones de inicio de sesión
        Instrucciones.ins_facial()

        # Limpia la pantalla
        print("\n" * 20)

        mis_imagenes = []
        nombres_empleados = []
        lista_empleados = os.listdir(ruta)

        # print(lista_empleados)

        for empleado in lista_empleados:
            imagen_actual = cv2.imread(f"{ruta}/{empleado}")
            mis_imagenes.append(imagen_actual)
            nombres_empleados.append(os.path.splitext(empleado)[0])

        # print (nombres_empleados)

        def codificar(imagenes):
            lista_codificada = []  # lista vacia

            for imagen in imagenes:
                imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)  # convertir de bgr a rgb
                codificado = fr.face_encodings(imagen)[0]  # donde está la cara en la imagen
                lista_codificada.append(codificado)  # agregar a la lista codificada

            return lista_codificada

        # funcion codificar imagenes para obteer las codificaciones de las caras
        lista_empleados_codificada = codificar(mis_imagenes)

        # print(lista_empleados_codificada) # imprimir la cantidad codificadas

        # tomar la foto de la camara
        captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        # leer la foto
        exito, imagen = captura.read()

        #cv2.imshow("Foto", imagen)
        #cv2.waitKey(0)

        # print("Exito: ", exito)

        # determinar si se puedo tomar la foto
        if not exito:
            print("No se pudo tomar la foto")
            captura.release()
            exit()
        else:
            # reconocer la cara en foto
            cara_captura = fr.face_locations(imagen)
            # codificar foto tomada
            cara_captura_codificada = fr.face_encodings(imagen, known_face_locations=cara_captura)

            for caracodif, caraubi in zip(cara_captura_codificada, cara_captura):
                coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif, 0.6)
                distancia = fr.face_distance(lista_empleados_codificada, caracodif)

            # print(coincidencias)
            # print(distancia)

            # indice de la coincidencia

            #print(indice_coincidencia)

            try:  # manejar las excepciones si no se encuentran coincidencias
                indice_coincidencia = numpy.argmin(distancia)
                if distancia[indice_coincidencia]:
                    print(f"Bienvenido {nombres_empleados[indice_coincidencia]}")
                    input("\nPresiones Enter para continuar.")
                    return True
                else:
                    # Opción para reintentar o cerrar el sistema
                    pregunta = input("No se encontraron coincidencias. \nPresione Enter para intentar de nuevo, o X para cerrar el sistema: ").lower()
                    captura.release()
                    if pregunta != "x":
                        var = self.facial()  # Llama recursivamente a la función para reintentar
                        return var
                    else:

                        return exit()  # Cierra el sistema si el usuario ingresa 'x'


            except:
                # Opción para reintentar o cerrar el sistema
                pregunta = input("No se encontraron coincidencias. \nPresione Enter para intentar de nuevo, o X para cerrar el sistema: ").lower()
                captura.release()
                if pregunta != "x":
                    var = self.facial()  # Llama recursivamente a la función para reintentar
                    return var
                else:

                    return exit()  # Cierra el sistema si el usuario ingresa 'x'



    def contrasenia(self):
        # Muestra las instrucciones de inicio de sesión
        Instrucciones.ins_login()

        # Limpia la pantalla
        print("\n" * 20)

        # Credenciales de acceso predeterminadas
        usuario = "admin"
        contrasenia = "admin123"
        contraseniaInversa = contrasenia[::-1]  # Invierte la contraseña
        acceso = False

        print("---INICIO DE SESION---\n")
        # Solicita al usuario ingresar sus credenciales
        usu = input("Ingrese el usuario: ")
        intento = input("Ingresa tu contraseña: ")
        intentoInverso = intento[::-1]  # Invierte la contraseña ingresada

        # Verifica si las credenciales ingresadas coinciden con las predeterminadas
        if usu == usuario and intento == contrasenia and intentoInverso == contraseniaInversa and contraseniaInversa[2::2] == intentoInverso[2::2]:
            acceso = True
            return acceso  # Retorna True si el acceso es exitoso

        else:
            # Informa al usuario que las credenciales son incorrectas
            print("\nUsuario o contraseña incorrectos.")

            # Opción para reintentar o cerrar el sistema
            pregunta = input("Presione Enter para intentar de nuevo, o X para cerrar el sistema: ").lower()

            if pregunta != "x":
                var = self.contrasenia()  # Llama recursivamente a la función para reintentar
                return var
            else:
                return exit()  # Cierra el sistema si el usuario ingresa 'x'

    def elegir_metodo(self, opcion):
        var = False
        menus = Menus()

        if opcion == "1":
            var = self.facial()
            return var
        elif opcion == "2":
            var = self.contrasenia()
            return var
        elif opcion == "3":
            return exit()
        elif opcion != "1" and opcion != "2" and opcion != "3":
            input("\nOpcion no valida, presione Enter para intentar de nuevo.")
            m = menus.login_menu()
            self.elegir_metodo(m)