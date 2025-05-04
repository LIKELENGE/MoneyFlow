from .charger_personnes import ChargerPersonnes
from .ecrire_personne import EcrirePersonnes
from models.personne import Personne
from flask import request
liste_personnes = ChargerPersonnes()

def ajouter_personne(nom, prenom, mail, sexe, date_naissance, mp):
    for personne in liste_personnes:
        if personne.mail == mail:
            raise ValueError("Cet email est déjà utilisé.")
    
    nouvelle_personne = Personne(nom, prenom, mail, sexe, date_naissance, mp)
    liste_personnes.append(nouvelle_personne)
    EcrirePersonnes(liste_personnes)

def verifier_mp(mail, mp):
    for personne in liste_personnes:
        if personne.mail == mail:
            if personne.verifier_mp(mp):
                return personne
            else:
                raise ValueError("Mot de passe incorrect.")
    raise ValueError("Personne non trouvée.")

    
def modifier_personne(mail, nom=None, prenom=None, sexe=None, date_naissance=None, mp=None):
    for personne in liste_personnes:
        if personne.mail == mail:
            if nom:
                personne.nom = nom
            if prenom:
                personne.prenom = prenom
            if sexe:
                personne.sexe = sexe
            if date_naissance:
                personne.date_naissance = date_naissance
            if mp:
                personne.mp = mp
            EcrirePersonnes(liste_personnes)
            return
    raise ValueError("Personne non trouvée.")

def supprimer_personne(mail):
    for personne in liste_personnes:
        if personne.mail == mail:
            liste_personnes.remove(personne)
            EcrirePersonnes(liste_personnes)
            return
    raise ValueError("Personne non trouvée.")


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

def ajouter_revenu(mail, revenu):
    personne = afficher_personne_par_mail(mail)
    if personne:
        personne.ajouter_revenu(revenu)
        EcrirePersonnes(liste_personnes)
    else:
        raise ValueError("Personne non trouvée.")