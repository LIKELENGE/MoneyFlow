from .charger_personnes import ChargerPersonnes
from .ecrire_personne import EcrirePersonnes
from models.personne import Personne
from flask import request
liste_personnes = ChargerPersonnes()

def ajouter_personne(nom, prenom, mail, sexe, date_naissance):
    for personne in liste_personnes:
        if personne.mail == mail:
            raise ValueError("Cet email est déjà utilisé.")
    
    nouvelle_personne = Personne(nom, prenom, mail, sexe, date_naissance)
    liste_personnes.append(nouvelle_personne)
    EcrirePersonnes(liste_personnes)


def afficher_liste_personnes():
    return liste_personnes

def afficher_personne_par_mail(mail):
    for personne in liste_personnes:
        if personne.mail == mail:
            return personne
    return None

def ajouter_depense(mail, depense):
    personne = afficher_personne_par_mail(mail)
    if personne:
        personne.ajouter_depense(depense)
        EcrirePersonnes(liste_personnes)
    else:
        raise ValueError("Personne non trouvée.")