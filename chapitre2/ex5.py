# Déclaration de la fonction
verif = lambda ch, c: ch.lower().startswith(c.lower())

# Demander à l'utilisateur de saisir une chaîne et un caractère
chaine = input("Veuillez saisir une chaîne : ")
c = input("Veuillez saisir un caractère : ")
if verif(chaine, c):
    print(f"La chaîne '{chaine}' commence par le caractère '{c}'")
else:
    print(f"La chaîne '{chaine}' ne commence pas par le caractère '{c}'")