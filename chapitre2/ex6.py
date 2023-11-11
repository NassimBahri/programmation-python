# Initialisation du dictionnaire
etudiants = [
    {"nom": "Etudiant 1", "note": 13.5},
    {"nom": "Etudiant 2", "note": 15},
    {"nom": "Etudiant 3", "note": 10},
    {"nom": "Etudiant 4", "note": 18}
]

# Trier la liste des étudiants par note obtenue (ordre croissant)
sorted_etudiants = sorted(etudiants, key=lambda e: e["note"])
print("Ordre croissant :", sorted_etudiants)

# Trier la liste des étudiants par note obtenue (ordre décroissant)
sorted_etudiants = sorted(etudiants, key=lambda e: e["note"], reverse=True)
print("Ordre décroissant :", sorted_etudiants)