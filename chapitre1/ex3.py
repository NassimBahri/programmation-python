# Demander à l'utilisateur de saisir son année de naissance
annee = int(input("Votre année de naissance : "))
# Demander à l'utilisateur si son anniversaire est déjà passé
anniversaire = input("Votre anniversaire est déjà passé ? (o/n) : ")
if anniversaire.lower() == "o":
    age = 2023 - annee
else:
    age = 2023 - annee - 1
# Afficher l'age
print(f"Votre age est : {age}")