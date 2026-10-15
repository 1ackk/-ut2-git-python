nota = float(input("Escribe tu nota: "))
calificacion = ""
if nota < 5:
 calificacion = "insuficiente"
elif nota < 6:
 calificacion = "Suficiente"
elif nota < 7:
 calificacion = "Bien"
elif nota < 9:
 calificacion = "Notable"
else:
 calificacion = "Sobresaliente"
print(f"Calificación: {calificacion}")