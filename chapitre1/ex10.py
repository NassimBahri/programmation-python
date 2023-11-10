# Créer le dictionnaire avec la méhode classique
nombres = dict()
for i in range(10):
    nombres[i] = "Pair" if i % 2 == 0 else "Impair"
print(nombres)

# Créer le dictionnaire avec Dictionary comprehension
nombres = {i: "Pair" if i % 2 == 0 else "Impair" for i in range(10)}
print(nombres)