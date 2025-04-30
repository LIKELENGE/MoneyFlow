import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.personne import Personne

def EcrirePersonnes(personnes):
    """
    Sauvegarde une liste de Personne dans le fichier JSON.
    :param personnes: Liste d'objets Personne
    """
    nom_fichier = "personnes.json"
    try:
        with open(nom_fichier, 'w') as f:
            data = [p.to_dict() for p in personnes]
            json.dump(data, f, indent=4)
            print(f"{len(personnes)} personnes enregistrées avec succès dans '{nom_fichier}'.")
    except Exception as e:
        print(f"Erreur lors de l'écriture du fichier '{nom_fichier}': {e}")
