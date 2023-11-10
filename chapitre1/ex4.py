# Demander à l'utilisateur de saisir un mois
mois = int(input("Veuillez saisir un mois : "))
if 9 <= mois <= 11:
    print("Automne")
elif mois == 12 or mois == 1 or mois == 2:
    print("Hiver")
elif 3 <= mois <= 5:
    print("Printemps")
elif 6 <= mois <= 8:
    print("Eté")
else:
    print("Valeur invalide")