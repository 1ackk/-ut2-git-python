nota = float(input("Escribe tu nota: "))
calificacion = ""
if 5 > nota >= 0:
    calificacion = "Suspenso"
elif 5 <= nota < 7:
    calificacion = "Aprobado"
elif 7 <= nota < 9:
    calificacion = "Notable"
elif 9 <= nota <= 10:
    calificacion = "Sobresaliente"
else:
    calificacion = "Nota no valida"
print(f"Calificación: {calificacion}")