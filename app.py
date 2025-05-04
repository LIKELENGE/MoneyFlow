from flask import Flask
from routes.routes_personnes import ajouter_personne_bp, afficher_personnes_bp, afficher_personne_par_mail_bp, ajouter_transaction_bp, supprimer_personne_bp, index_bp, verifier_mp_bp

app = Flask(__name__) 

app.register_blueprint(ajouter_personne_bp)
#app.register_blueprint(afficher_personnes_bp)
app.register_blueprint(afficher_personne_par_mail_bp)
app.register_blueprint(ajouter_transaction_bp)
app.register_blueprint(supprimer_personne_bp)
app.register_blueprint(index_bp)
app.register_blueprint(verifier_mp_bp)

if __name__ == "__main__":
    app.run(debug=True)
