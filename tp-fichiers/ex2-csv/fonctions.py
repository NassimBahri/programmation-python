# Importer les modules CSV et ceil
import csv
from math import ceil


# Fonction qui permet de créer le fichier contenant la formule globale pour chaque candidat
def formule_gen():
    with open("PSI.csv", "r") as input, open("PSI_FG.csv", "w") as output:
        file_reader = csv.reader(input, delimiter=',')
        file_writer = csv.writer(output, delimiter=',')
        for line in file_reader:
            fg = (float(line[3]) * 5 + float(line[4])) * int(line[5])
            enregistrement = [line[0], line[1], line[2], str(round(fg, 2))]
            file_writer.writerow(enregistrement)


# Fonction qui permet de classer les candidats
def classer():
    with open("PSI_FG.csv", "r") as file:
        file_reader = csv.reader(file, delimiter=',')
        lines = []
        for line in file_reader:
            lines.append(line)
        sorted_lines = sorted(lines, key=lambda l: float(l[3]), reverse=True)
    with open("PSI_FG.csv", "w") as file:
        file_writer = csv.writer(file, delimiter=',')
        file_writer.writerows(sorted_lines)
    print("---- TERMINE ----")


# Générer les listes principale et attente
def generer():
    with open("PSI_FG.csv", "r") as file:
        file_reader = csv.reader(file, delimiter=',')
        candidats = []
        for line in file_reader:
            candidats.append(line)
    with open("PSI_P.csv", "w") as principale, open("PSI_A.csv", "w") as attente:
        nb_lignes = len(candidats)
        nb_principale = ceil(nb_lignes * 0.7)
        file_writer_principale = csv.writer(principale, delimiter=',')
        file_writer_attente = csv.writer(attente, delimiter=',')
        file_writer_principale.writerows(candidats[:nb_principale])
        file_writer_attente.writerows(candidats[nb_principale:])

# Afficher les détails d'un candidat
def afficher(num_insc):
    with open("PSI_FG.csv", "r") as file:
        file_reader = csv.reader(file, delimiter=',')
        position = 0
        candidats = []
        for line in file_reader:
            candidats.append(line)
        count = len(candidats)
        for candidat in candidats:
            position += 1
            if candidat[0] == num_insc:
                if position <= ceil(0.7 * count):
                    print(f"Le candidat {candidat[1]} est dans la liste principale")
                else:
                    print(f"Le candidat {candidat[1]} est dans la liste d'attente")