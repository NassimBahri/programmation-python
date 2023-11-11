# Déclaration de la fonction
def saisir():
    resultat = dict()
    for i in range(5):
        x = int(input(f"Veuillez saisir un nombre {i + 1} : "))
        resultat[x] = [value for value in range(1, x) if x % value == 0]
    return resultat

# Tester la fonction
resultat = saisir()
print(resultat)