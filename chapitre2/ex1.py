# Déclaration de la fonction
def min_max(*nombres):
    min_value = nombres[0]
    max_value = nombres[0]
    for i in range(1, len(nombres)):
        if nombres[i] > max_value:
            max_value = nombres[i]
        if nombres[i] < min_value:
            min_value = nombres[i]
    return min_value, max_value

# Appel de la fonction
v_min, v_max = min_max(10, 125, 624, 1547, -30)
print(f"La valeur minimale est : {v_min}")
print(f"La valeur maximale est : {v_max}")