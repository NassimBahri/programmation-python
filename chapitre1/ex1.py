# Demander à l'utilisateur de saisir un entier
nombre = int(input("Veuillez saisir un entier X : "))
if nombre < 0:
    print(f"La valeur absolue du nombre saisi est : {-nombre}")
else:
    print(f"La valeur absolue du nombre saisi est : {nombre}")