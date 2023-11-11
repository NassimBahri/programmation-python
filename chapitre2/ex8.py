# Déclaration de la fonction
def chiffre_porte_bonheur(nb):
    while nb >=10:
        somme = 0
        for x in str(nb):
            somme += int(x) ** 2
        nb = somme
    return nb == 1

# Demander à l'utilisateur de saisir un nombre
nombre = int(input("Veuillez saisir un nombre : "))
if chiffre_porte_bonheur(nombre):
    print(f"{nombre} est un chiffre porte Bonheur")
else:
    print(f"{nombre} n'est pas un chiffre porte Bonheur")