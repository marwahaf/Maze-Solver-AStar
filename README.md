# Maze-Solver- A* Pathfinding 

## Description
Ce projet implémente l'algorithme de recherche de chemin A* pour trouver le chemin le plus court dans un labyrinthe. L'algorithme explore efficacement la meilleure route entre un point de départ et une destination tout en évitant les obstacles. Une visualisation est intégrée avec Pygame pour afficher le labyrinthe et le chemin calculé.

## Fonctionnalités
- Implémente l'algorithme A* avec l'heuristique de distance Manhattan.
- Prend en charge des labyrinthes fournis par l'utilisateur ou générés aléatoirement.
- Fournit une visualisation graphique du labyrinthe, incluant les cellules bloquées et non bloquées.
- Affiche le chemin le plus court calculé entre la source et la destination.

## Prérequis
- Python 3.12
- NumPy
- Pygame

## Installation
Assurez-vous que Python est installé, puis installez les dépendances requises :
```sh
pip install -r requirements.txt
```

**Notes :** Il est possible d'utiliser un docker , toutefois , il n'a pas été configuré pour lancer la GUI. (Je ne sais pas comment le faire hehe)

## Utilisation
1. Exécutez le script :
   ```sh
   python main.py
   ```
2. Choisissez d'entrer votre propre labyrinthe ou d'en générer un aléatoirement.
3. Entrez les coordonnées de la source et de la destination.
4. Le script calculera le chemin le plus court et l'affichera graphiquement.

## Structure des fichiers
- `main.py` : Implémente l'algorithme A* et gère les entrées utilisateur.
- `visualize.py` : Contient la logique de visualisation avec Pygame.
- `requirements.txt` : Liste des dépendances requises.

## Détails de l'algorithme A*
L'algorithme A* fonctionne comme suit :
1. Initialisation de la liste ouverte avec le nœud de départ.
2. Expansion du nœud ayant le plus faible coût total (`f = g + h`).
3. Mise à jour des nœuds voisins et suivi des parents.
4. Répétition jusqu'à atteindre la destination ou constater qu'aucun chemin n'est trouvable.
5. Reconstruction du chemin optimal en remontant les parents.

### Visualisation
- Le labyrinthe est représenté sous forme de grille avec des couleurs distinctes :
  - **Cellules bloquées** : Gris
  - **Position de départ** : Rouge
  - **Destination** : Bleu
  - **Chemin trouvé** : Vert

## Exemple
```
Entrer le labyrinthe sous forme matricielle : [[1, 1, 1], [0, 1, 0], [1, 1, 1]]
Entrer le point de départ : (0, 0)
Entrer le point de destination : (2, 2)
```
**Sortie** : Le chemin le plus court est affiché dans la fenêtre Pygame.

## Limitations
- L'algorithme suppose une grille avec des coûts de déplacement uniformes.
- Il ne supporte pas le mouvement en diagonale.

## Améliorations futures
- Ajouter le support du mouvement en diagonale avec heuristiques adaptées.
- Améliorer l'interface utilisateur pour une meilleure interaction.
- Implémenter d'autres algorithmes de recherche de chemin pour comparaison.

---

# Famille d'algorithmes de recherche de chemin

- **Breadth-First Search (BFS)** : Explore uniformément dans toutes les directions.
- **Dijkstra** : Prend en compte les coûts de déplacement.
- **A*** : Dirige l'exploration vers la destination en utilisant une heuristique.

### A* fonctionne avec :
- **G (coût réel)** : Distance parcourue depuis le point de départ.
- **H (heuristique)** : Estimation de la distance restante (Manhattan ou Euclidienne).
- **F (coût total)** : `F = G + H`, utilisé pour choisir le meilleur chemin.

### Logique de l'algorithme :
1. Démarrer avec le nœud de départ et l'ajouter à la liste ouverte.
2. Explorer les nœuds voisins (haut, bas, gauche, droite).
3. Calculer `F = G + H` pour chaque voisin.
4. Sélectionner le nœud ayant le plus faible `F`.
5. Répéter jusqu'à atteindre la destination.
6. Reconstruire le chemin le plus court.

---

# Heapq : Gestion des priorités

## Qu'est-ce qu'un tas (Heap) ?
Un tas est une structure de données en arbre binaire où chaque parent est soit :
- Plus petit ou égal à ses enfants (min-heap).
- Plus grand ou égal à ses enfants (max-heap).

Dans un **min-heap**, le plus petit élément est toujours à la racine, ce qui permet d'extraire rapidement le nœud ayant le coût le plus bas. C'est ce qui est utilisé dans A* pour gérer la liste des nœuds à explorer efficacement.

## Ressources inspirantes
- [Red Blob Games - A* Pathfinding](https://www.redblobgames.com/pathfinding/a-star/introduction.html)
