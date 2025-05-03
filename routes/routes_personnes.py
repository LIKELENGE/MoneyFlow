from flask import Blueprint, request, jsonify, render_template
from views.personne_view import ajouter_personne, afficher_liste_personnes, afficher_personne_par_mail
from views.personne_view import ajouter_depense
from models.depense import Depense

ajouter_personne_bp = Blueprint('ajouter_personne', __name__)
afficher_personnes_bp = Blueprint('afficher_personnes', __name__)
afficher_personne_par_mail_bp = Blueprint('afficher_personne_par_mail', __name__)  # 🔧 Nom corrigé ici
ajouter_depense_bp = Blueprint('ajouter_depense', __name__)

@ajouter_personne_bp.route('/ajouter_personne', methods=['GET'])
def afficher_formulaire_ajouter_personne():
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
        ajouter_personne(nom, prenom, mail, sexe, date_naissance)
        print(f"Personne à ajouter: Nom={nom}, Prénom={prenom}, Email={mail}, Sexe={sexe}, Date={date_naissance}")
        return jsonify({"message": "Personne ajoutée avec succès"}), 201
    except KeyError as e:
        return jsonify({"error": f"Champ manquant: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"Erreur interne : {str(e)}"}), 500

@afficher_personnes_bp.route('/afficher_personnes', methods=['GET'])
def afficher_personnes():
    personnes = afficher_liste_personnes()
    return render_template('afficher_personnes.html', personnes=personnes)

@afficher_personne_par_mail_bp.route('/personne/<mail>', methods=['GET'])
def afficher_personne(mail):
    print(f"Recherche de la personne avec l'e-mail : {mail}")
    personne = afficher_personne_par_mail(mail)
    if personne:
        print(f"Personne trouvée : {personne}")
        return render_template('afficher_personne.html', personne=personne)
    else:
        print("Personne non trouvée.")
        return jsonify({"error": "Personne non trouvée"}), 404
    
@ajouter_depense_bp.route('/personne/<mail>', methods=['POST'])
def ajouter_depense_route(mail):
    try:
        data = request.form  # Utilisé pour form HTML
        montant = data['montant']
        date = data['date']
        description = data['description']
        depense = Depense(montant, date, description)
        ajouter_depense(mail, depense)

        personne = afficher_personne_par_mail(mail)
        return render_template("afficher_personne.html", personne=personne, message="Dépense ajoutée avec succès")
    except KeyError as e:
        return f"Erreur : champ manquant {str(e)}", 400




# def get_personne_par_mail(mail):
#     """Récupère une personne par son adresse e-mail."""
#     personnes = afficher_liste_personnes
#     for personne in personnes:
#         if personne["mail"] == mail:
#             return personne
#     return None