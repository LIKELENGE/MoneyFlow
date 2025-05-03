from .transaction import Transaction

class Revenu(Transaction):
    def __init__(self, montant, date, description):
        super().__init__(montant, date, description)