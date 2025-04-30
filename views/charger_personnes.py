import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
from models.personne import Personne
from models.revenu import Revenu
from models.depense import Depense


def ChargerPersonnes():
    """
    Charge les personnes à partir d'un fichier JSON.
    :return: Une liste d'objets Personne.
    """
    nom_fichier = "personnes.json"
    try:
        with open(nom_fichier, 'r') as f:
            data = json.load(f)
            personnes = [Personne.from_dict(item) for item in data]
            return personnes
    except FileNotFoundError:
        print(f"Le fichier '{nom_fichier}' n'existe pas.")
        return []
    except json.JSONDecodeError:
        print(f"Erreur de décodage JSON dans le fichier '{nom_fichier}'.")
        return []

# Test simple
personnes = ChargerPersonnes()
for p in personnes:
    print(p)
