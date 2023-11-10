# Demander à l'utilisateur de saisir un nombre
nombre = input("Veuillez saisir un nombre : ")
exists = False
i = 0
while i < len(nombre) -1 and not exists:
    j = i + 1
    while j < len(nombre) and not exists:
        if nombre[i] == nombre[j]:
            exists = True
        j += 1
    i += 1

if not exists:
    print(f"{nombre} est un nombre disctint")
else:
    print(f"{nombre} n'est pas un nombre disctint")
