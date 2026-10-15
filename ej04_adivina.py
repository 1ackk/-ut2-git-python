import random

secreto = random.randint(1, 20)
intentos = 0
while True:
    num = int(input("Adivina el numero (1-20): "))
    intentos = intentos + 1
    if num == secreto:
        print(f"¡Acertaste en {intentos} intentos!")
        break
    elif num < secreto:
        print("Es mayor")
    else:
        print("Es menor")
