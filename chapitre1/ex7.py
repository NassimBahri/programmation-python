# Demander à l'utilisateur de saisir un nombre
nombre = input("Veuillez saisir un nombre : ")

## Solution 1 : Manipulation d'une chaîne de caractères
somme = 0
for x in nombre:
    somme += int(x) ** 3
if somme == int(nombre):
    print(f"{nombre} est un nombre Armstrong")
else:
    print(f"{nombre} n'est pas un nombre Armstrong")

## Solution 2 : Manipulation d'un entier
nombre_copie = int(nombre)  # Conversion
somme = 0
while nombre_copie > 0:
    reste = nombre_copie % 10
    somme += reste ** 3
    nombre_copie = nombre_copie // 10
if somme == int(nombre):
    print(f"{nombre} est un nombre Armstrong")
else:
    print(f"{nombre} n'est pas un nombre Armstrong")