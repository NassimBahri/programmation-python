# Ouvrir le fichier en mode lecture
with open("students.txt", "r") as content:
    line_number = 1
    for line in content:
        print(line_number, ":", line.strip())
        line_number += 1