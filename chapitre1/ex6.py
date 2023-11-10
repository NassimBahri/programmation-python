# Demander à l'utilisateur de saisir un nombre a
a = float(input("Veuillez saisir un nombre a : "))
# Demander à l'utilisateur de saisir un nombre b
b = float(input("Veuillez saisir un nombre b : "))
# Demander à l'utilisateur de saisir un opérateur
op = input("Veuillez saisir un opérateur (+, -, /, *) : ")
if op == "+":
    print(f"{a} + {b} = {a + b}")
elif op == "-":
    print(f"{a} - {b} = {a - b}")
elif op == "*":
    print(f"{a} * {b} = {a * b}")
elif op == "/":
    if b == 0:
        print("Opération invalide (division par zéro)!")
    else:
        print(f"{a} / {b} = {a / b}")
else:
    print("Opérateur invalide!")