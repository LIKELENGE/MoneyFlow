from flask import Flask, render_template, request, redirect, url_for
from models.personne import Personne
from forms import AjouterPersonneForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'une_cle_secrete_tres_securisee'  # Important pour Flask-WTF

# Liste pour stocker les personnes (en mémoire pour cet exemple simple)
liste_personnes = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ajouter_personne', methods=['GET', 'POST'])
def ajouter_personne():
    form = AjouterPersonneForm()
    if form.validate_on_submit():
        nom = form.nom.data
        prenom = form.prenom.data
        mail = form.mail.data
        sexe = form.sexe.data
        date_naissance = form.date_naissance.data.strftime('%Y-%m-%d')

        # Vérification de la doublure de l'e-mail
        for personne in liste_personnes:
            if personne.mail == mail:
                return render_template('ajouter_personne.html', form=form, erreur_mail='Cet email est déjà utilisé.')

        nouvelle_personne = Personne(nom, prenom, mail, sexe, date_naissance)
        liste_personnes.append(nouvelle_personne)
        return redirect(url_for('afficher_personnes'))
    return render_template('ajouter_personne.html', form=form)

@app.route('/personnes')
def afficher_personnes():
    return render_template('afficher_personnes.html', personnes=liste_personnes)

if __name__ == '__main__':
    app.run(debug=True)