def menu():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("---INGRESE LO QUE DESEA HACER---")
    print("1. Ver su departamento y municipios junto con su edad.")
    print("2. Ver solo su municipio")
    print("3. Salir")

    deseo = int(input("\nColoque el numero de la opcion(1, 2 o 3): "))

    return deseo