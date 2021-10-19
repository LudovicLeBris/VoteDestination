
# Vote destinations

## Description

Petit script Python avec interface web en Flask pour comptabiliser des votes pour choisir une destination de vacances.  
Le script enregsitre le prénom du votant dans un fichier json et refaire un vote avec même prénom n'est pas permis.   
Un lien invisible en bas à gauche sous les boutons de vote permet d'accèder à la page de résultat. Il est invisible pour ne pas influencer les votants et permetre à l'organisateur de savoir quelle destination à été choisie.

Le script "Vote.py" est autonome et sert d'API pour l'interface.

## Versions utilisés
### Environnement
- Python 3.9
- Pip 21.2.4
### Packages (voir requirement.txt)
- click 8.0.1
- colorama 0.4.4
- Flask 2.0.1
- itsdangerous 2.01
- Jinja2 3.0.1
- MarkupSafe 2.0.1
- Werkzeug 2.0.1


## Lancement
Il faudra au préalable installer un environnement virtuel et installer les packages nécessaires depuis le fichier "requirements.txt"
Pour lancer l'interface Flask  utilisé la commande ```Flask run```  
Cela lance un serveur Flask en local et la page d'accueil est accessible à cette adresse : http://127.0.0.1:5000