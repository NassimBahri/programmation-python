# Déclaration de la fonction qui permet de vérifier si un nombre est premier ou non
def is_premier(n):
    is_valid = True
    i = 2
    while i < n and is_valid:
        if n % i == 0:
            is_valid = False
        i += 1
    return is_valid

# Déclaration de la fonction principale
def principale(m, n):
    # Syntaxe de la liste comprehension
    return [value for value in range(m, n+1) if is_premier(value)]

# Demander à l'utilisateur de saisir deux nombres m et n (m < n)
m = 0
n = 0
while True:
    m = int(input("Veuillez saisir nombre m : "))
    n = int(input(f"Veuillez saisir un nombre n > {m} : "))
    if m < n:
        break
# Tester la fonction principale
resultat = principale(m, n)
print(resultat)