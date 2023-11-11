# Déclaration d'une liste d'étudiants vide
liste_etudiants = []

# Déclaration de la fonction saisir
def saisir():
    insert = True
    while insert:
        nom = input("Veuillez saisir le nom de l'étudiant : ")
        code = int(input("Veuillez saisir le code de l'étudiant : "))
        module = input("Veuillez saisir le nom du module : ")
        note = float(input("Veuillez saisir la note de l'étudiant : "))
        if verif(code, module):
            print("Ce couple (code/module) existe déjà")
            continue
        liste_etudiants.append({
            "nom": nom,
            "code": code,
            "module": module,
            "note": note
        })
        decision = input("Ajouter un nouvel étudiant ? (o/n) : ")
        if decision.lower() != "o":
            insert = False

# Déclaration de la fonction qui permet de vérifier l'existance du couple (code/module)
def verif(code, module):
    exists = False
    i = 0
    while i < len(liste_etudiants) and not exists:
        etudiant = liste_etudiants[i]
        if etudiant["code"] == code and etudiant["module"] == module:
            exists = True
        i += 1
    return exists

# Déclaration de la fonction qui permet de calculer la moyenne d'un étudiant
def moyenne(code_etudiant):
    somme = 0
    nb_matieres = 0
    for etudiant in liste_etudiants:
        if etudiant["code"] == code_etudiant:
            somme += etudiant["note"]
            nb_matieres += 1
    if nb_matieres > 0:
        return somme / nb_matieres
    else:
        return 0

# Déclaration de la fonction qui permet de récupérer la liste des étudiants admis
def admis():
    # Les variables "admis" et "not_admis" permet d'indiquer si nous avons déjà traité l'étudiant ou non
    admis = set() # Permet de sauvegarder le code des étudiants admis
    not_admis = set()  # Permet de sauvegarder le code des étudiants non admis
    resultat = []
    for etudiant in liste_etudiants:
        if etudiant["code"] not in admis and etudiant["code"] not in not_admis:
            # Dans ce cas nous allons calculer la moyenne de l'étudiant
            moyenne_etudiant = moyenne(etudiant["code"])
            if moyenne_etudiant >= 10:
                admis.add(etudiant["code"])
                resultat.append({
                    "nom": etudiant["nom"],
                    "moyenne": moyenne_etudiant
                })
            else:
                not_admis.add(etudiant["code"])
    return sorted(resultat, key=lambda e: e["moyenne"], reverse=True)


# Tester le code
saisir() # Pour remplit la liste des étudiants
etudiants_admis = admis() # Récupérer les étudiants admis
# Afficher les étudiants admis
print("Etudiants admis :", etudiants_admis)