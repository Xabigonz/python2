#Número Aleatorio del 1 al 100.

#Con while:

import random

numeroAdiv = random.randint(0, 100)

while True:
    pregunta = int(input("Intenta adivinar el número aleatorio del 1 al 100: "))
    if pregunta < numeroAdiv:

        print(f"El numero es mayor, ")

    elif pregunta > numeroAdiv:

        print(f"El numero es menor, ")

    else:

        print (f"El numero es correcto, es {numeroAdiv}")
        break


# Reto Adivina el numero con FOR
import random

rnd = random.randint(1, 100)

vidas =5
print("Adivina el numero entre el 1 y 100")
print(f"Tienes {vidas} intentos para adivinar el número secreto entre 1 y 10.")
print("------------------------------------------------------------")

for vida in range(vidas):
    # Mientras que vida se encuentre en el rango vidas entra
    res = int(input("Introduce un numero entero : "))
    if rnd != res:
        vidas_restantes = vidas - vida
        if res > rnd:
            print(f"El número misterioso es menor que {res}. Te quedan {vidas_restantes} intentos.")

        else:
            print(f"El número misterioso es mayor que {res}. Te quedan {vidas_restantes} intentos.")
    else:
        print("¡Felicidades, has acertado!")
        break  # Sale del bucle for

else:
    print(f"Lo siento, el número secreto era {rnd}. ¡Mejor suerte la próxima vez!")