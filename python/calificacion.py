calif = int(input("Intruzca tu calificacion"))
if calif < 0:
    print("Error: Calif insuficiente")
elif calif < 5:
    print("reprovado")
elif calif == 5:
    print("Suficiente")
elif calif == 6:
    print("aprobado")
elif calif == 7:
    print("notable")
elif calif >= 8:
    print("sobresaliente")