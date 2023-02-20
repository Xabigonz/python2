dnis = []
dniYedades = ['DFENFE87X', 19, 'EFJBFE', 22]
edades = []
while True:
    print(f"---------------------------------------------------------------------------------------------------------")
    caso=int(input(f"Menu: \n 1 para mostrar la lista de empleados \n 2 para añadir empleados y su edad \n 3 para eliminar a empleado \n 4 para modificar la edad de un empleado \n 5 para salir del menu"
                 f"\n Eliga una opcion : \n"))

    match caso:

        case 1:
            print(f"{dniYedades}")
        case 2:
            DNI = input("Dime cual es su nombre :")
            while DNI in dnis:
                print(f"El empleado {DNI} ya existe")
                DNI = input("Dime cual su dni :")
            else:
                dnis.append(DNI)
                edad = float(input(f"Cual es la edad de {DNI} : "))
                while edad<18 or edad>65:
                    print(f"Lo siento esas {edad} esta fuera del rango de la empresa")
                else:
                    edades.append(edad)
                    print(f"Se ha integrado a {DNI} correctamente y su edad es {edad}")
                    dniYedades.append((DNI, str(edad)))
        case 3:
            DNI = input("Dime el DNI del empleado que quieres eliminar: ")
            for i in dniYedades:
                if i[0] == dnis:
                    dniYedades.remove(i)
                    dnis.remove(DNI)
                    edades.remove(edad[1])
                    print(f"El empleado con DNI {DNI} ha sido eliminado.")
                    break
            else:
                print(f"No se encontró el empleado {DNI}")
        case 4:
            DNI = input("Dime el DNI del empleado: ")
            for i, empleado in enumerate(dniYedades):
                if empleado[0] == DNI:
                    edad = empleado[1]
                    print(f"La nota actual de {empleado[0]} es {edad}")
                    edadNueva = float(input(f"Dime la nota nueva para {empleado[0]}: "))
                    edades[i] = edadNueva
                    print(f"La nota de {empleado[0]} ha sido actualizada a {edadNueva}")

            else:
                print(f"No se encontró el alumno con DNI {DNI}")
        case 5:
            break
    print(f"---------------------------------------------------------------------------------------------------------")