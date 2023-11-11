# Déclaration de la fonction
def count(chaine):
    nb_maj = 0
    nb_min = 0
    for c in chaine:
        if c.islower():
            nb_min += 1
        elif c.isupper():
            nb_maj += 1
    return nb_maj, nb_min

# Demander à l'utilisateur de saisir une chaîne de caractères
chaine = input("Veuillez saisir une chaîne de caractères : ")
# Appel de la fonction
nb_maj, nb_min = count(chaine)
print(f"Le nombre de lettre en majuscule est : {nb_maj}")
print(f"Le nombre de lettre en miniscule est : {nb_min}")