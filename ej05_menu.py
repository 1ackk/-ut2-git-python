print("1. Saludar")
print("2. Despedirse")
print("3. Salir")
opcion = input("Elige una opcion: ")
match opcion:
    case "1":
        print("¡Hola!")
    case "2":
        print("¡Adios!")
    case "3":
        print("Saliendo...")
    case _:
        print("Opcion no valida")
