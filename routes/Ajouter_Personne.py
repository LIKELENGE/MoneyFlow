from flask import Blueprint, request, jsonify, render_template
from views.personne_view import AjouterPersonne
ajouter_personne_bp = Blueprint('ajouter_personne', __name__)

@ajouter_personne_bp.route('/ajouter_personne', methods=['GET'])
def afficher_formulaire_ajouter_personne():
    """Affiche le formulaire pour ajouter une personne."""
    return render_template('ajouter_personne.html')

@ajouter_personne_bp.route('/ajouter_personne', methods=['POST'])
def ajouter_personne_route():
    try:
        data = request.form # Utilisez request.form pour les données de formulaire
        nom = data['nom']
        prenom = data['prenom']
        mail = data['mail']
        sexe = data['sexe']
        date_naissance = data['date_naissance']

        AjouterPersonne(nom, prenom, mail, sexe, date_naissance)
        # Appelez votre fonction pour ajouter la personne (par exemple, dans un modèle)
        # AjouterPersonne(nom, prenom, mail, sexe, date_naissance)
        print(f"Personne à ajouter: Nom={nom}, Prénom={prenom}, Email={mail}, Sexe={sexe}, Date={date_naissance}")

        return jsonify({"message": "Personne ajoutée avec succès"}), 201

    except KeyError as e:
        return jsonify({"error": f"Champ manquant: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"Erreur interne : {str(e)}"}), 500