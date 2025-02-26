# SecurePass - Gestionnaire de mots de passe sécurisé
SecurePass est un gestionnaire de mots de passe développé en Python, permettant de générer, enregistrer, afficher, modifier et supprimer des mots de passe de manière sécurisée. Les mots de passe sont cryptés à l'aide de la bibliothèque cryptography et stockés dans une base de données SQLite.

## Fonctionnalités

Générer un mot de passe : Génère des mots de passe aléatoires de longueur personnalisée.

Enregistrer un mot de passe : Sauvegarde un mot de passe dans une base de données SQLite, après l'avoir chiffré.

Voir les mots de passe enregistrés : Affiche tous les mots de passe enregistrés (déchiffrés à la volée).

Modifier un mot de passe : Permet de modifier un mot de passe existant.

Supprimer un mot de passe : Supprime un mot de passe existant de la base de données.

## Structure du projet

Le projet est composé de trois scripts Python principaux :

1. start.py

Ce script crée la clé de chiffrement et la base de données nécessaires pour l'application.

Création de la clé de chiffrement : Si la clé n'existe pas, elle est générée et sauvegardée dans un fichier encryption.key.

Création de la base de données SQLite : Une base de données appelée password_manager.db est créée si elle n'existe pas.

2. delete.py

Ce script permet de supprimer la clé de chiffrement et la base de données.

Suppression des fichiers : Si la base de données ou la clé existent, elles sont supprimées.

3. app.py

Ce script est le cœur de l'application. Il permet à l'utilisateur d'interagir avec le gestionnaire de mots de passe via une interface en ligne de commande.

Génération de mot de passe : L'utilisateur peut générer un mot de passe aléatoire.
Enregistrement et gestion des mots de passe : L'utilisateur peut enregistrer, afficher, modifier ou supprimer des mots de passe.
Chiffrement des mots de passe : Lors de l'enregistrement ou de la modification des mots de passe, ceux-ci sont chiffrés avec la clé de chiffrement.

## Installation - Prérequis

pip install -r requirements.txt

Étapes d'installation

Clonez le repository :

git clone https://github.com/Sekhmet23z/SecurePass.git

cd securepass

Exécutez start.py pour créer la base de données et la clé de chiffrement :

python3 start.py ou ./start.py

Ce script va créer un fichier encryption.key pour la clé de chiffrement et une base de données password_manager.db.

Utilisez app.py pour interagir avec l'application :

python3 app.py ou ./app.py

Vous serez accueilli avec un menu permettant de gérer vos mots de passe.

Supprimez les fichiers avec delete.py (si nécessaire) :

python3 delete.py ou ./delete.py

Ce script supprimera la base de données et la clé de chiffrement.

##Utilisation

Une fois l'application lancée via app.py, un menu interactif s'affichera dans le terminal :

Générer un mot de passe : Génère un mot de passe aléatoire de longueur personnalisée.

Enregistrer un mot de passe : Demande un nom de mot de passe et un mot de passe (ou génère un mot de passe si vide).

Voir les mots de passe enregistrés : Affiche la liste des mots de passe enregistrés dans la base de données.

Modifier un mot de passe : Permet de changer un mot de passe existant.

Supprimer un mot de passe : Supprime un mot de passe de la base de données.

Quitter : Quitte l'application.

##Sécurité

Les mots de passe sont stockés dans la base de données SQLite sous forme chiffrée.
Seule la clé de chiffrement encryption.key permet de les déchiffrer.

Licence
Ce projet est sous licence MIT. Vous pouvez l'utiliser et le modifier à votre guise.
