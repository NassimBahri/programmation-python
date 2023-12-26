# Importer le module CSV
import csv


# Fonction qui permet de saisir la liste des candidats
def saisir():
    with open("concours.csv", "w") as file:
        file_writer = csv.writer(file, delimiter=',')
        ajouter = "o"
        while ajouter.lower() == "o":
            cin = input("NCIN : ")
            nom = input("Nom : ")
            prenom = input("Prénom : ")
            age = input("Age : ")
            decision = input("Décision : admis, refusé, ajourné : ")
            file_writer.writerow([cin, nom, prenom, age, decision])
            ajouter = input("Voulez-vous ajouter un nouveau condidat (o/n) ?")


# Liste des admis
def admis():
    with open("concours.csv", "r") as file, open("admis.csv", "w") as admis:
        file_reader = csv.reader(file, delimiter=',')
        file_writer = csv.writer(admis, delimiter=',')
        for line in file_reader:
            if line[4] == "admis":
                file_writer.writerow(line)


# Liste d'attente
def attente():
    liste_attente = []
    with open("admis.csv", "r") as admis:
        file_reader = csv.reader(admis, delimiter=',')
        for line in file_reader:
            if int(line[3]) > 30:
                data = [line[0], line[1], line[2]]
                liste_attente.append(data)
    with open("attente.csv", "w") as attente:
        file_writer = csv.writer(attente, delimiter=',')
        file_writer.writerows(liste_attente)


# Statistique
def stat(dec):
    with open("concours.csv", "r") as file:
        file_reader = csv.reader(file, delimiter=',')
        total = 0
        nombre = 0
        for line in file_reader:
            total += 1
            if line[4] == dec:
                nombre += 1
        return nombre / total * 100


# Supprimer les candidats âgés plus que 30 (Méthode 1)
def supprimer():
    with open("admis.csv", "r") as file:
        file_reader = csv.reader(file, delimiter=',')
        liste_finale = []
        for line in file_reader:
            if int(line[3]) <= 30:
                liste_finale.append(line)
    with open("admis.csv", "w") as file:
        file_writer = csv.writer(file, delimiter=',')
        file_writer.writerows(liste_finale)
