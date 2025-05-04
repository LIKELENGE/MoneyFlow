import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.personne import Personne

def EcrirePersonnes(personnes):
    nom_fichier = "personnes.json"
    try:
        with open(nom_fichier, 'w') as f:
            data = [p.to_dict() for p in personnes]
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Erreur lors de l'écriture du fichier '{nom_fichier}': {e}")
