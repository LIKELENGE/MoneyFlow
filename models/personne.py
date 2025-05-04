import bcrypt
from .revenu import Revenu
from .depense import Depense

class Personne:
    def __init__(self, nom, prenom, mail, sexe, date_naissance, mp, depenses=None, revenus=None):
        self.mail = mail
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe
        self.date_naissance = date_naissance
        self.mp = self.crypter_mp(mp)
        self.depenses = depenses if depenses is not None else []
        self.revenus = revenus if revenus is not None else []
        self.total_revenus = self.calculer_total_revenus()
        self.total_depenses = self.calculer_total_depenses()
    
    def crypter_mp(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def verifier_mp(self, mp):
        return bcrypt.checkpw(mp.encode('utf-8'), self.mp.encode('utf-8'))
        
    
    def calculer_total_revenus(self):
        return sum(revenu.montant for revenu in self.revenus) if self.revenus else 0

    def calculer_total_depenses(self):
        return sum(depense.montant for depense in self.depenses) if self.depenses else 0

    @property
    def solde(self):
        return self.total_revenus - self.total_depenses


    def ajouter_depense(self, depense):
        self.depenses.append(depense)

    def ajouter_revenu(self, revenu):
        self.revenus.append(revenu)
        
    def __str__(self):
        depenses_str = "\n    ".join(str(dep) for dep in self.depenses) if self.depenses else "Aucune dépense"
        revenus_str = "\n    ".join(str(rev) for rev in self.revenus) if self.revenus else "Aucun revenu"
        return (
            f"Personne: {self.prenom} {self.nom} ({self.mail})\n"
            f"  Sexe: {self.sexe}\n"
            f"  Date de naissance: {self.date_naissance}\n"
            f"  Dépenses:\n    {depenses_str}\n"
            f"  Revenus:\n    {revenus_str}"
        )

    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        return {
            'nom': self.nom,
            'prenom': self.prenom,
            'mail': self.mail,
            'sexe': self.sexe,
            'date_naissance': self.date_naissance,
            'mp': self.mp,
            'depenses': [dep.to_dict() for dep in self.depenses],
            'revenus': [rev.to_dict() for rev in self.revenus]
        }
    @staticmethod
    def from_dict(data):
        depenses = [Depense.from_dict(dep) for dep in data.get('depenses', [])]
        revenus = [Revenu.from_dict(rev) for rev in data.get('revenus', [])]
        return Personne(
            nom=data['nom'],
            prenom=data['prenom'],
            mail=data['mail'],
            sexe=data['sexe'],
            date_naissance=data['date_naissance'],
            mp=data['mp'],
            depenses=depenses,
            revenus=revenus)
    
    def verifier_mp(self, mp):
        return self.mp == mp