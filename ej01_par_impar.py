num = 0
try: 
    num = int(input("Introduce un numero entero: "))
except ValueError:
    print("ERR0R: El valor que has introducido no es un error.")
    exit()
else:
    if num % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")
# Autor: Compañero
