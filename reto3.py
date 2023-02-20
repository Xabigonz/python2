dnis = []
dniYnotas = ['Prueba1', 7.25, 'Carmelo', 5.32]
notas = []
while True:
    print(f"---------------------------------------------------------------------------------------------------------")
    caso=int(input(f"Menu: \n 1 para mostrar la lista de alumnos \n 2 para añadir alumnos y su nota \n 3 para eliminar a alumnos \n 4 para modificar la nota de un alumno \n 5 para salir del menu"
                 f"\n Eliga una opcion : \n"))

    match caso:

        case 1:
            print(f"{dniYnotas}")
        case 2:
            DNI = input("Dime cual es su nombre :")
            while DNI in dnis:
                print(f"El alumno {DNI} ya existe")
                DNI = input("Dime cual es su nombre :")
            else:
                dnis.append(DNI)
                nota = float(input(f"Cual es la nota de {DNI} : "))
                notas.append(nota)
                print(f"Se ha integrado a {DNI} correctamente y su nota es {nota}")
                dniYnotas.append((DNI, str(nota)))
        case 3:
            DNI = input("Dime el DNI del alumno que quieres eliminar: ")
            for i in dniYnotas:
                if i[0] == dnis:
                    dniYnotas.remove(i)
                    dnis.remove(DNI)
                    notas.remove(nota[1])
                    print(f"El alumno con DNI {DNI} ha sido eliminado.")
                    break
            else:
                print(f"No se encontró el alumno {DNI}")
        case 4:
            DNI = input("Dime el DNI del alumno: ")
            for i, alumno in enumerate(dniYnotas):
                if alumno[0] == DNI:
                    nota = alumno[1]
                    print(f"La nota actual de {alumno[0]} es {nota}")
                    notaNueva = float(input(f"Dime la nota nueva para {alumno[0]}: "))
                    notas[i] = notaNueva
                    print(f"La nota de {alumno[0]} ha sido actualizada a {notaNueva}")

            else:
                print(f"No se encontró el alumno con DNI {DNI}")
        case 5:
            break
    print(f"---------------------------------------------------------------------------------------------------------")