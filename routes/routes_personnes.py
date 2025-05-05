import bcrypt
from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from views.personne_view import ajouter_personne, afficher_liste_personnes, afficher_personne_par_mail, modifier_personne, supprimer_personne, verifier_mp
from views.personne_view import ajouter_depense, ajouter_revenu
from models.depense import Depense
from models.revenu import Revenu

ajouter_personne_bp = Blueprint('ajouter_personne', __name__)
afficher_personnes_bp = Blueprint('afficher_personnes', __name__)
afficher_personne_par_mail_bp = Blueprint('afficher_personne_par_mail', __name__)
ajouter_transaction_bp = Blueprint('ajouter_transaction', __name__)
modifier_personne_bp = Blueprint('modifier_personne', __name__)
supprimer_personne_bp = Blueprint('supprimer_personne', __name__)
verifier_mp_bp = Blueprint('verifier_mp', __name__)
index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def index():
    return render_template('index.html')


@ajouter_personne_bp.route('/ajouter_personne', methods=['GET'])
def afficher_formulaire_ajouter_personne():
    return render_template('ajouter_personne.html')

@ajouter_personne_bp.route('/ajouter_personne', methods=['POST'])
def ajouter_personne_route():
    try:
        data = request.form
        nom = data['nom']
        prenom = data['prenom']
        mail = data['mail']
        sexe = data['sexe']
        date_naissance = data['date_naissance']
        mp = data['mp']
        mp_confirmation = data['mp_confirmation']

        if mp != mp_confirmation:
            return render_template("ajouter_personne.html", error="Les mots de passe ne correspondent pas.")

        ajouter_personne(nom, prenom, mail, sexe, date_naissance, mp)
        personne = afficher_personne_par_mail(mail)
        return render_template("afficher_personne.html", personne=personne)

    except KeyError as e:
        return render_template("ajouter_personne.html", error=f"Champ manquant: {str(e)}")
    except Exception as e:
        return render_template("ajouter_personne.html", error=f"Erreur interne : {str(e)}")



@verifier_mp_bp.route('/verifier_mp', methods=['POST'])
def verifier_mp_route():
    try:
        data = request.form
        mp = data['mp']
        mail = data['mail']
        personne = verifier_mp(mail, mp)
        return render_template('afficher_personne.html', personne=personne)
    except KeyError as e:
        return jsonify({"error": f"Champ manquant: {str(e)}"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne : {str(e)}"}), 500



@modifier_personne_bp.route('/modifier_personne/<mail>', methods=['POST'])
def modifier_personne_route(mail):
    try:
        data = request.form
        nom = data.get('nom')
        prenom = data.get('prenom')
        sexe = data.get('sexe')
        date_naissance = data.get('date_naissance')
        
        modifier_personne(mail, nom, prenom, sexe, date_naissance)
        return jsonify({"message": "Personne modifiée avec succès"}), 200
    except KeyError as e:
        return jsonify({"error": f"Champ manquant: {str(e)}"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": f"Erreur interne : {str(e)}"}), 500



@supprimer_personne_bp.route('/supprimer_personne/<mail>', methods=['POST'])
def supprimer_personne_route(mail):
    try:
        supprimer_personne(mail)
        return redirect(url_for('index.index'))
    except ValueError as e:
        return jsonify({"error": str(e)}), 200
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
    
@ajouter_transaction_bp.route('/personne/<mail>', methods=['POST'])
def ajouter_transaction_route(mail):
    try:
        data = request.form
        montant = data['montant']
        date = data['date']
        description = data['description']
        categorie = data.get('categorie', "inconnu")
        type_transaction = data['type_transaction']

        if type_transaction == "revenu":
            transaction = Revenu(montant, date, description, categorie)
            ajouter_revenu(mail, transaction)
        else:
            transaction = Depense(montant, date, description, categorie)
            ajouter_depense(mail, transaction)

        personne = afficher_personne_par_mail(mail)
        return render_template("afficher_personne.html", personne=personne, message="Transaction ajoutée avec succès")

    except KeyError as e:
        return f"Erreur : champ manquant {str(e)}", 400

