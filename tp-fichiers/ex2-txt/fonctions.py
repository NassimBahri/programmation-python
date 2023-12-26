from math import ceil


# Fonction qui permet de créer le fichier contenant la formule globale pour chaque candidat
def formule_gen():
    with open("PSI.txt", "r") as input, open("PSI_FG.txt", "w") as output:
        for line in input:
            data = line.strip().split(",")
            fg = (float(data[3]) * 5 + float(data[4])) * int(data[5])
            enregistrement = data[0] + "," + data[1] + "," + data[2] + "," + str(round(fg, 2))
            output.write(enregistrement + "\n")


# Fonction qui permet de classer les candidats
def classer():
    with open("PSI_FG.txt", "r") as file:
        lines = file.readlines()
        sorted_lines = sorted(lines, key=lambda l: float(l.strip().split(",")[3]), reverse=True)
    with open("PSI_FG.txt", "w") as file:
        file.writelines(sorted_lines)
    print("---- TERMINE ----")


# Générer les listes principale et attente
def generer():
    with open("PSI_FG.txt", "r") as file:
        candidats = file.readlines()
    with open("PSI_P.txt", "w") as principale, open("PSI_A.txt", "w") as attente:
        nb_lignes = len(candidats)
        nb_principale = ceil(nb_lignes * 0.7)
        principale.writelines(candidats[:nb_principale])
        attente.writelines(candidats[nb_principale:])

# Afficher les détails d'un candidat
def afficher(num_insc):
    with open("PSI_FG.txt", "r") as file:
        position = 0
        candidats = file.readlines()
        count = len(candidats)
        for candidat in candidats:
            position += 1
            data = candidat.strip().split(",")
            if data[0] == num_insc:
                if position <= ceil(0.7 * count):
                    print(f"Le candidat {data[1]} est dans la liste principale")
                else:
                    print(f"Le candidat {data[1]} est dans la liste d'attente")