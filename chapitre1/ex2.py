# Demander à l'utilisateur de saisir une chaîne
chaine = input("Veuillez saisir une chaîne de caractères : ")
# Récupérer le premier caractère
first = chaine[0]
# Récupérer le dernier caractère
last = chaine[-1]
# Afficher le réultat final
resultat = last + chaine[1:-1] + first
print(resultat)