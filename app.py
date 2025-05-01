from flask import Flask
from routes.Ajouter_Personne import ajouter_personne_bp

app = Flask(__name__)  # <= ici __name__

app.register_blueprint(ajouter_personne_bp)

if __name__ == "__main__":
    app.run(debug=True)
