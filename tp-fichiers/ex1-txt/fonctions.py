# Fonction qui permet de saisir la liste des candidats
def saisir():
    with open("concours.txt", "w") as f:
        ajouter = "o"
        while ajouter.lower() == "o":
            cin = input("NCIN : ")
            nom = input("Nom : ")
            prenom = input("Prénom : ")
            age = input("Age : ")
            decision = input("Décision : admis, refusé, ajourné : ")
            f.write(cin + ";" + nom + ";" + prenom + ";" + age + ";" + decision + "\n")
            ajouter = input("Voulez-vous ajouter un nouveau condidat (o/n) ?")

# Liste des admis
def admis():
    with open("concours.txt", "r") as file, open("admis.txt", "w") as admis:
        liste_admis = []
        for line in file:
            data = line.strip().split(";")
            if data[4] == "admis":
                liste_admis.append(line)
        admis.writelines(liste_admis)

# Liste d'attente
def attente():
    liste_attente = []
    with open("admis.txt", "r") as admis:
        for line in admis:
            data = line.strip().split(";")
            if int(data[3]) > 30:
                liste_attente.append(data[0] + ";" + data[1] + ";" + data[2] + "\n")
    with open("attente.txt","w") as attente:
        attente.writelines(liste_attente)

# Statistique
def stat(dec):
    with open("concours.txt", "r") as file:
        lines = file.readlines()
        total = len(lines)
        nombre = 0
        for line in lines:
            data = line.strip().split(";")
            if data[4] == dec:
                nombre += 1
        return nombre / total * 100

# Supprimer les candidats âgés plus que 30 (Méthode 1)
def supprimer():
    with open("admis.txt", "r") as file:
        lines = file.readlines()
        liste_finale = []
        for line in lines:
            data = line.split(";")
            if int(data[3]) <= 30:
                liste_finale.append(line)
    with open("admis.txt", "w") as file:
        file.writelines(liste_finale)

# Supprimer les candidats âgés plus que 30 (Méthode 2)
def supprimer2():
    with open("admis.txt", "r") as file:
        lines = file.readlines()
        for i in range(0, len(lines)):
            data = lines[i].split(";")
            if int(data[3]) > 30:
                del lines[i]
    with open("admis.txt", "w") as file:
        file.writelines(lines)