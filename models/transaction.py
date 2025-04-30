class Transaction:
    def __init__(self, montant, date, description):
        self.montant = montant
        self.date = date
        self.description = description

    def to_dict(self):
        return {
            'montant': self.montant,
            'date': self.date,
            'description': self.description
        }