# Importer les fonctions à utiliser
from fonctions import saisir, admis, attente, stat, supprimer

# Ajouter des candidats
# saisir()

# Créer le fichier des admis
admis()

# Créer la liste d'attente
attente()

# Afficher le pourcentage des candidats admis
pourcentage_admis = stat("admis")
print(f"Le pourcentage des candidats admis est {pourcentage_admis}%")

# Supprimer les candidats
supprimer()