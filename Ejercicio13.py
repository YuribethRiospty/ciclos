palabra = input(" Escribe una palabra: ")
vocales = 0 
for letra in palabra.lower():
    if letra in "aeiou":
        vocales += 1 
print("Tiene", vocales, "vocales")
