dnis = []
dni_edades = {'DFENFE87X': 19, 'EFJBFE': 22}

edades = []
while True:
    print(f"---------------------------------------------------------------------------------------------------------")
    caso = int(input(f"Menu: \n 1 para mostrar la lista de empleados \n 2 para añadir empleados y su edad \n 3 para eliminar a empleado \n 4 para modificar la edad de un empleado \n 5 para salir del menu"
                     f"\n Eliga una opcion : \n"))

    match caso:

        case 1:
            print(f"{dni_edades}")
        case 2:
            DNI = input("Dime cual es su DNI :")
            while DNI in dnis:
                print(f"El empleado {DNI} ya existe")
                DNI = input("Dime cual su dni :")
            else:
                dnis.append(DNI)
                edad = int(input(f"Cual es la edad de {DNI} : "))
                while edad <= 18 or edad >= 65:
                    print(
                        f"Lo siento esas {edad} esta fuera del rango de la empresa")
                    edad = float(input(f"Cual es la edad de {DNI} : "))
                else:
                    edades.append(edad)
                    print(
                        f"Se ha integrado a {DNI} correctamente y su edad es {edad}")
                    dni_edades.update({DNI: edades})
        case 3:
            DNI = input("Dime el DNI del empleado que quieres eliminar: ")
            if DNI in dni_edades:
                del dni_edades[DNI]
                print(f"El empleado con DNI {DNI} ha sido eliminado.")
            else:
                print(f"No se encontró el empleado {DNI}")
        case 4:
            DNI = input("Dime el DNI del empleado: ")
            if DNI in dni_edades:
                edad_actual = dni_edades[DNI]
                print(f"La edad actual de {DNI} es {edad_actual}")
                edad_nueva = int(input(f"Dime la nueva edad para {DNI}: "))
                dni_edades[DNI] = edad_nueva
                print(f"La edad de {DNI} ha sido actualizada a {edad_nueva}")
            else:
                print(f"No se encontró el empleado con DNI {DNI}")

        case 5:
            break
    print(f"---------------------------------------------------------------------------------------------------------")
