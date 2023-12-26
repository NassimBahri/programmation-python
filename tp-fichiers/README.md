# TP : Gestion des fichiers

## Exercice 1

Soit un fichier intitulé ``concours.txt`` qui comporte les enregistrements relatifs aux candidats d’un concours. Chaque enregistrement est composé des champs suivants : NCIN, NOM, PRENOM, AGE, DECISION : (type contenant les identificateurs suivants : admis, refusé, ajourné), et séparé par point virgule (;).

**Travail demandé :**

1. Définir la fonction ``saisir()`` qui permet de remplir les données relatives aux candidats dans le fichier ``concours.txt``.

2. Définir la fonction ``admis()`` qui permet créer le fichier ``admis.txt`` comportant les données relatives aux candidats admis.

3. Afin de sélectionner en priorité les candidats admis et âgés moins de 30 ans, créer la fonction ``attente()`` qui produira à partir du fichier ``admis.txt``, un nouveau fichier intitulé ``attente.txt`` comportant les données relatives aux candidats admis et âgés plus que 30 ans. Une ligne du fichier ``attente.txt`` comprend le NCIN, le NOM et PRENOM d’un candidat séparés par point virgule (;).

4. Définir la fonction ``statistiques(dec)`` qui permet de retourner le pourcentage des candidats pour la décision dec (admis, refusé et ajourné). Exemple : Le pourcentage des candidats admis = (Nombre des candidats admis / Nombre des candidats) *100.

5. Définir la fonction ``supprimer()`` qui supprimera du fichier ``admis.txt`` les candidats âgés plus que 30.

[Correction de l'exercice (format txt)](ex1-txt) | [Correction de l'exercice (format csv)](ex1-csv)

## Exercice 2

Après la réussite au baccalauréat, les meilleurs bacheliers sont orientés vers les classes préparatoires aux grandes écoles. En effet, la priorité est à celui qui a le score (nombre de points) le plus élevé. Ce score est appelé formule globale. Les élèves admissibles seront classés par ordre décroissant selon la formule globale, Puis, une fois classés, ces bacheliers seront divisés en 2 groupes de la façon suivante :

| Groupe            | NB. étudiants |
| -----------       | -----------   |
| Liste principale  | 30            |
| Liste d’attente   | 40            |

On dispose d’un fichier nommé ``PSI.txt`` contenant la liste des bacheliers admissibles de la section Physique et sciences industrielles. Dans ce fichier, chaque bachelier est défini par :

* Num insc : le numéro d’inscription
* NP : le nom et prénom
* FILIERE : le nom de la filière (SMA, SMB, PC ou SVT)
* MG : moyenne générale.
* FS (formule spécifique) : un réel déjà calculé à partir des notes obtenues dans les diverses matières.
* i : un réel = 1 si l’élève est redoublant en BAC et 2 sinon.

**Travail demandé :**

1. Définir la fonction ``formule_gen()`` qui permet de créer un autre fichier ``PSI_FG.txt``, à partir du fichier ``PSI.txt``, et y stocker, pour les mêmes bacheliers, les informations suivantes : Num insc, NP, FILIERE et FG. Sachant que la formule globale (FG) de chaque élève est calculée comme suit : ``FG=((5*MG+FS)*i)``.

2. Définir la fonction ``classer()`` qui permet de classer les bacheliers du fichiers ``PSI FG.txt`` par ordre décroissant selon la formule globale.

3. Définir la fonction ``generer()`` qui permet d’extraire, dans le même répertoire, 2 autres fichiers (``PSI_principal.txt``, ``PSI_attente.txt``) contenant respectivement les bacheliers appartenant aux groupes : liste principale et liste d’attente.

4. Définir la fonction ``afficher(Num_insc)`` qui permet d’afficher, pour un candidat donné, en fonction de son numéro d’inscription (donnée fournie en argument), le groupe auquel il appartient.

[Correction de l'exercice (format txt)](ex2-txt) | [Correction de l'exercice (format csv)](ex2-csv)