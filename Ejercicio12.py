secreto = 7 
intento = int(input("Adivina el número (1 al 10): "))
while intento != secreto:
    if intento < secreto:
        print("Muy bajo")
    else:
        print("Muy alto")
    intento = int(input("Intenta de nuevo: "))
print("¡Acertaste!")
