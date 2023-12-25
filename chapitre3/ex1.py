# Déclaration d'un dictionnaire pour stocker le nombre d'oaccurence de chaue nom
names = dict()

###################
# Méthode 1
###################
# Ouvrir le fichier en mode lecture
with open("noms.txt", "r") as content:
    for name in content:
        name = name.strip()
        if name in names:
            names[name] += 1
        else:
            names[name] = 1

###################
# Méthode 2
###################
# Ouvrir le fichier en mode lecture
with open("noms.txt", "r") as content:
    for name in content:
        name = name.strip()
        names[name] = names.get(name, 0) + 1


# Afficher le nombre d'occurence de chaque nom
for name, nb in names.items():
    print(name, nb)