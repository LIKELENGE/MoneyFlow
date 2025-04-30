from revenu import Revenu
from depense import Depense

class Personne:
    def __init__(self, nom, prenom, mail, sexe, date_naissance):
        self.mail = mail
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe
        self.date_naissance = date_naissance
        self.depenses = []
        self.revenus = []

    def ajouter_depense(self, depense):
        self.depenses.append(depense)

    def ajouter_revenu(self, revenu):
        self.revenus.append(revenu)

    def to_dict(self):
        return {
            'nom': self.nom,
            'prenom': self.prenom,
            'mail': self.mail,
            'sexe': self.sexe,
            'date_naissance': self.date_naissance,
            'depenses': [dep.to_dict() for dep in self.depenses],
            'revenus': [rev.to_dict() for rev in self.revenus]
        }
    