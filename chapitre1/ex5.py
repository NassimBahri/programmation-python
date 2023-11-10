# Demander à l'utilisateur de saisir une année
annee = int(input("Veuillez saisir une année : "))
if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
    print(f"{annee} est une année bissextile")
else:
    print(f"{annee} n'est pas une année bissextile")