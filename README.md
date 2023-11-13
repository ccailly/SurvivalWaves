- **Titre** du jeu
- **Description** courte du jeu
- **🎯 Contexte & cahier des charges** : développé dans le cadre d'une formation, pour un formateur pour monter en compétence en Python ...
- **🎲 Règles** du jeu : maquette, déroulé d'une partie, conditions de victoire
- **🎮 Use cases**: 
    - pour l'administrateur : expliquer ce que peut/doit faire un administrateur qui souhaite lancer/administrer une arène de jeu avec des apprenants 
    - pour le joueur : renvoyer vers README API
- **🖧 Architecture matériel** (optionnel, peut être décrit avec le diagramme de séquence) : schéma overview présentant les machines et protocoles (serveurs, clients, broker) avec texte expliquant le choix des technologies 
- **📞 Diagramme de séquence**: expliquer le déroulé d'une partie, les principales étapes à faire dans l'ordre et qui/quoi/comment, les couches s'échangent quelles données pour qui/pour quoi
- **✅ Pré-requis** 
    - matériel et logiciel requis pour executer votre projet, pour l'administrateur 
    - pour les apprenants rediriger vers README API
- **⚙️ Installation** : step by step (commandes à executer par l'administrateur, paquets à installer ...)
- **🧪 Tests**: 
    - définition du plan de test ce qu'on attend quand on fait quoi 
    - step by step pour lancer les tests
- **🛣️ Roadmap**
- **🧑‍💻 Auteur**
- **⚖️ License**

# SurvivalWaves

## Maquette

### Map

![Map](doc/map.jpeg)

### Zombie

![Zombie](doc/zombie.png)

## UserStories:
  * **En tant que Joueur** :
    * Je peux me déplacer d'une case par tick
    * Je peux attaquer les zombies à l'aide d'une arme à feu
    * Tuer un zombie redonne instantanément des munitions
    * Je peux récupérer une arme par terre pour améliorer mes stats de dégats
    * Je peux ramasser des trousses de soins par terre et me soigne
    * Je peux voir toutes les unités joueur/objets/non-joeurs de la carte
    * Je peux améliorer mes stats de vie/dégats au fur et à mesure du nombre de zombies que je tue
* **En tant que zombie** :
    * Je peux me déplacement aléatoirement
    * Je peux détecter un humain dans un rayon X pour lui foncer dessus
    * Je peux détecter un humain à nimporte quel distance si il me tire dessus
    * Je peux attaquer et transformer un humain en X coups
    * Je ne peux pas ramasser d'armes
* **En tant qu'Arbitre** :
    * Je peux lancer une nouvelle vague
    * Je peux faire apparaitre des objets au début d'une vague
    * Je peux faire réaparaitre tout les joueurs à chaque nouvelle manche
    * Je peux afficher les changement de manche
    * Je peux faire apparaitre des zombies
    * Je peux augmenter le nombres de zombies à chaque vague et/ou améliorer leurs stats
    * A la fin d'une manche, je peux modifier le score de la manche dans le scoreboard
    * Si tout les survivants sont mort, je met fin à la vague en cours et note le nombre de manches passé dans le scoreboard
