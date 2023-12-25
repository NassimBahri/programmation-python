# Importer la méthode
from os.path import exists

###################
# Méthode 1
###################
# Vérfier l'existance du fichier "students.txt"
if not exists("students.txt"):
    print("Le fichier demandé n'existe pas!")
else:
    # Ouvrir les fichiers
    with open("students.txt", "r") as input, open("outputdata.txt", "w") as output:
        for line in input:
            output.write(line)
    print("Opération terminée avec succès!")


###################
# Méthode 2
###################
# Vérfier l'existance du fichier "students.txt"
if not exists("students.txt"):
    print("Le fichier demandé n'existe pas!")
else:
    # Ouvrir les fichiers
    with open("students.txt", "r") as input, open("outputdata.txt", "w") as output:
        lines = input.readlines()
        output.writelines(lines)
    print("Opération terminée avec succès!")