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


#Con for: y el "RANGE" para poder limitar los intentos:

vidas = range(0,3)

for numeroAdiv in vidas:
    pregunta = int(input("Intenta adivinar el número aleatorio del 1 al 100: "))
    if pregunta < numeroAdiv:
        
        print(f"El numero es mayor, ")
   
    elif pregunta > numeroAdiv:

        print(f"El numero es menor, ")

    else:

        print (f"El numero es correcto, es {numeroAdiv}")
        break

# Fin del archio loco