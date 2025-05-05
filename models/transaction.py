from datetime import datetime
import uuid

class Transaction:
    def __init__(self, montant, date, description, categorie = "inconnu", id=None):
        self.id = id or str(uuid.uuid4())
        self.montant = float(montant)
        self.date = date  # peut être une chaîne 'YYYY-MM-DD'
        self.description = description
        self.categorie = categorie
        
    def to_dict(self):
        return {
            'id': self.id,
            'montant': self.montant,
            'date': self.date,
            'description': self.description
        }

    @staticmethod
    def from_dict(data):
        return Transaction(
            id=data.get('id'),
            montant=data['montant'],
            date=data['date'],
            description=data['description']
        )

    def afficher_transaction_par_mois(self, mois, annee):
        """Vérifie si la transaction correspond au mois et à l'année donnés."""
        try:
            date_obj = datetime.strptime(self.date, '%Y-%m-%d')
            return date_obj.month == mois and date_obj.year == annee
        except ValueError:
            return False

    def __str__(self):
        return f"Transaction(id={self.id}, montant={self.montant}, date={self.date}, description='{self.description}')"

    def __repr__(self):
        return self.__str__()
