# Exercice de révision

On souhaite créer une application permettant de gérer les notes des étudiants pour les différents modules enseignés. Les données seront représentées avec une liste de dictionnaires nommé "`liste_etudiants`" et qui aura la forme suivante :
`[{"code": 1111, "nom": "Etudiant 1", "note" : 15,module" : "math"},...]`

## Question 1

Écrire une fonction `saisir()` qui permet de remplir les données relatives aux étudiants dans le dictionnaire "`liste_etudiants`". Cette fonction permet d’ajouter un nombre illumité d’étudiants. A chaque fois elle demande à l’utilisateur s’il souhaite ajouter un nouvel étudiant ou non. Il est aussi important de noter que le code de l’étudiant est unique (Vous pouvez créer une fonction qui vérifie l’existance du code/module). Pour l’ajout d’un étudiant, l’utilisateur saisie dans un premier lieu le nom du module, par la suite, il introduit les données relatives à l’étudiant.

## Question 2

Écrire une fonction `moyenne(code_etudiant)` qui permet de calculer la moyenne générale d’un étudiant bien précis. Il est à noter que tous les modules ont le même coefficient.

## Question 3

Écrire une fonction `admis()` qui permet de renvoyer la liste des étudiants admis. Le résultat envoyé sera sous la forme suivante : 
`[ {"nom": "Etudiant 3", "moyenne": 15.75},
{"nom": "Etudiant 1", "moyenne": 15.51},
{"nom": "Etudiant 8", "moyenne": 14.79} ]`

<ins>Il est aussi important de noter que la liste des étudiants admis sera triée dans un ordre décroissant selon la moyenne des étudiants.</ins>