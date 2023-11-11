# Chapitre 2 : Fonctions, modules et packages en Python

## Exercice 1

Écrire une fonction qui prend en paramètre un nombre arbitraire d'éléments et revoie la valeur maximale et la valeur minimale. [Correction de l'exercice](ex1.py)

## Exercice 2

Écrire une function Python qui prend une chaîne de caractères et calcule le nombre de lettres en majuscule et le nombre de lettres en miniscule. [Correction de l'exercice](ex2.py)

## Exercice 3

Écrire un programme en Python sous forme de fonction qui prends deux nombres `m` et `n` en paramètres (`m < n`) et qui renvoie une liste formée de tous les nombres premiers compris entre `m` et `n`.

Exemple : pour `m = 10` et `n = 20` la fonction doit renvoyer `[11, 13 , 17 , 19]`. [Correction de l'exercice](ex3.py)

## Exercice 4

Écrire un programme en Python sous forme de fonction qui demande à l’utilisateur de saisir dix nombres entiers de son choix et de lui renvoyer un dictionnaire dont les clés sont les entiers saisis et dont les valeurs sont les listes des diviseurs des nombres saisis.

Exemple : si l’utilisateur saisi les nombres : `2, 7, 11, 5, 3, 19, 14, 9, 1, 4`, le programme renvoie le dictionnaire : `d = {2: [1, 2], 7: [1, 7], 14: [1, 2, 7, 14], 9: [1, 3, 9], 11: [1, 11], 5: [1, 5] , 23: [1, 3], 19: [1, 19], 1: [1], 4: [1, 2, 4]}`. [Correction de l'exercice](ex4.py)

## Exercice 5

Écrire un programme python qui permet de trouver si une chaîne commence par un caractère donné en utilisant Lambda. [Correction de l'exercice](ex5.py)

## Exercice 6

Écrire un programme python qui permet de trier une liste de dictionnaires en utilisant la fonction Lambda. Vous pouvez utiliser la function `sorted()`. [Correction de l'exercice](ex6.py)

## Exercice 7

Écrire un programme permettant de jouer au jeu suivant : un nombre est tiré de manière aléatoire entre 1 et 100. Un joueur essaie de deviner ce nombre en proposant des nombres.

A chaque tentative le programme indique si le nombre à trouver est plus petit ou plus grand que le nombre du joueur. La partie s’achève lorsque le joueur trouve la bonne solution

Le programme affiche alors : Bravo ! Le nombre est bien ... Vous l’avez trouvé en ... coups. [Correction de l'exercice](ex7.py)

## Exercice 8

Écrire une fonction `chiffre_porte_bonheur(nb)` qui permet de déterminer si un nombre entier `nb` est chiffre porte Bonheur ou non.

* Un nombre chiffre porte Bonheur est un nombre entier qui, lorsqu’on ajoute les carrés de chacun de ses chiffres, puis les carrés des chiffres de ce résultat et ainsi de suite jusqu’à l’obtention d’un nombre à un seul chiffre égal à 1 (un)
* Le calcule s’arrête lorsque le chiffre devient inférieur `a 10.

Exemple : \
Nombre de depart : 913\
9^2=81\
1^2=1\
3^2=9\
Nouveau : 81+1+9=91\
9^2=81\
1^2=1\
Nouveau : 81+1=82\
8^2=64\
2^2=4\
Nouveau : 64+4=68\
6^2=36\
8^2=64\
Nouveau : 36+64=100\
1^2=1\
0^2=0\
0^2=0\
Nouveau : 1+0+0=1\
Le chiffre : 913 est un porte boneur.
 [Correction de l'exercice](ex8.py)
