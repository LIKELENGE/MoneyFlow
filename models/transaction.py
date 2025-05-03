from datetime import datetime

class Transaction:
    def __init__(self, montant, date, description):
        self.montant = montant
        self.date = date  # ici date peut rester une string pour l’instant
        self.description = description

    def to_dict(self):
        return {
            'montant': self.montant,
            'date': self.date,  # assure-toi que c'est une chaîne formatée 'YYYY-MM-DD'
            'description': self.description
        }

    @staticmethod
    def from_dict(data):
        return Transaction(
            montant=data['montant'],
            date=data['date'],
            description=data['description']
        )
    def __str__(self):
        return f"Transaction(montant={self.montant}, date={self.date}, description='{self.description}')"
    def __repr__(self):
        return self.__str__()