from .transaction import Transaction

class Revenu(Transaction):
    def __init__(self, montant, date, description, categorie="inconnu", id=None):
        super().__init__(montant, date, description, categorie, id)
