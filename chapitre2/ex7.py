# Importer le package qui permet de faire des opérations de type aléatoire
import random

# Tirer un nombre aléatoire
guess = random.randint(1, 100)
print(guess)

# Demander à l'utilisateur de jouer
nb_coups = 0
is_valid = False
while not is_valid:
    nombre = int(input("Veuillez deviner le nombre : "))
    nb_coups += 1
    if nombre > guess:
        print("Veuillez choisir un nombre plus petit!")
    elif nombre < guess:
        print("Veuillez choisir un nombre plus grand!")
    else:
        is_valid = True
        print(f"Bravo! Le nombre est bien. Vous l'avez trouvé en {nb_coups} coups")