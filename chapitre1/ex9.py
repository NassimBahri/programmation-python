# Initialiser une liste vide
liste_nombres = []
# Demander à l'utilisateur de saisir la liste des nombres
for i in range(10):
    nombre = int(input(f"Veuillez saisir le nombre {i + 1} : "))
    if nombre not in liste_nombres:
        liste_nombres.append(nombre)
if len(liste_nombres) == 10:
    print("Tous les nombres sont disctincts")
else:
    print("Les nombres ne sont pas disctincts")