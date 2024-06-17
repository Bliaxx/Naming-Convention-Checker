Documentation de l'outil de validation des conventions de nommage des assets
Table des matières
Introduction
Configuration
Exemple d'utilisation
Dépannage

1. Introduction
Cet outil a été conçu pour valider les conventions de nommage des assets dans les projets Unreal Engine. Il vérifie que les assets respectent les conventions de nommage définies dans un fichier de configuration et génère un rapport des assets non conformes.

2. Configuration
Le fichier de configuration naming_conventions.json doit être placé dans le répertoire Config de votre projet Unreal Engine. Ce fichier doit contenir un dictionnaire JSON définissant les conventions de nommage pour chaque classe d'asset.

Exemple de naming_conventions.json :

json
Copier le code
{
    "Texture2D": "T_",
    "Material": "M_",
    "StaticMesh": "SM_"
}

3. Exemple d'utilisation
Pour exécuter l'outil de validation des conventions de nommage, suivez les étapes ci-dessous :

Placez le fichier de configuration naming_conventions.json dans le répertoire Config de votre projet.
Exécutez le script principal naming_convention_checker.py (ouvrez Unreal puis Tools -> Execute Python Script)
Le script analysera les assets de votre projet dans le répertoire "Game" et générera un rapport des assets non conformes.

4. Dépannage
Problème : Aucun asset n'est détecté
Assurez-vous que le chemin du répertoire de contenu du projet est correct.
Vérifiez que les classes d'assets dans le fichier de configuration naming_conventions.json correspondent aux classes d'assets utilisées dans votre projet.
Problème : Tous les assets sont signalés comme conformes
Vérifiez que les conventions de nommage dans le fichier de configuration sont correctes.
Ajoutez des logs supplémentaires pour déboguer le script et vérifier les chemins des assets.