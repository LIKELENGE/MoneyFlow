import json
import datetime
import random
import os
from transaction import Transaction
from revenu import Revenu
from depense import Depense
from personne import Personne

listes_personne = []

# Liste de noms et prénoms pour générer des personnes aléatoirement
noms = ["Dubois", "Leroy", "Moreau", "Garcia", "Bernard", "Petit"]
prenoms_hommes = ["Jean", "Pierre", "Michel", "Alain", "Philippe"]
prenoms_femmes = ["Sophie", "Nathalie", "Isabelle", "Claire", "Sandrine"]
domaines_mail = ["example.com", "work.net", "personal.org"]
sexes = ["M", "F", "X"]

# Liste de descriptions pour les revenus et dépenses
descriptions_revenus = ["Salaire", "Remboursement", "Intérêts", "Prime", "Allocation"]
descriptions_depenses = ["Loyer", "Courses", "Transport", "Loisirs", "Facture", "Restaurant", "Shopping"]

def generer_date_aleatoire(start_year=2024, end_year=2025):
    start = datetime.date(start_year, 1, 1)
    end = datetime.date(end_year, 12, 31)
    time_between_dates = end - start
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start + datetime.timedelta(days=random_number_of_days)
    return random_date.strftime("%Y-%m-%d")

def generer_date_naissance_aleatoire(start_year=1970, end_year=2000):
    start = datetime.date(start_year, 1, 1)
    end = datetime.date(end_year, 12, 31)
    time_between_dates = end - start
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start + datetime.timedelta(days=random_number_of_days)
    return random_date.strftime("%Y-%m-%d")

def generer_personne_aleatoire():
    nom = random.choice(noms)
    prenom = random.choice(prenoms_hommes + prenoms_femmes)
    mail = f"{prenom.lower()}.{nom.lower()}@{random.choice(domaines_mail)}"
    sexe = random.choice(sexes)
    date_naissance = generer_date_naissance_aleatoire()
    personne = Personne(nom, prenom, mail, sexe, date_naissance)
    # Ajouter des revenus aléatoires
    for _ in range(random.randint(2, 5)):
        montant = round(random.uniform(50, 3000), 2)
        date = generer_date_aleatoire()
        description = random.choice(descriptions_revenus)
        personne.ajouter_revenu(Revenu(montant, date, description))
    # Ajouter des dépenses aléatoires
    for _ in range(random.randint(3, 7)):
        montant = round(random.uniform(10, 500), 2)
        date = generer_date_aleatoire()
        description = random.choice(descriptions_depenses)
        personne.ajouter_depense(Depense(montant, date, description))
    return personne

# Création de plusieurs personnes aléatoires
nombre_de_personnes = 3
for _ in range(nombre_de_personnes):
    listes_personne.append(generer_personne_aleatoire())

# Fonction pour sauvegarder la liste des personnes au format JSON en ajoutant aux données existantes
def sauvegarder_personnes_json(liste_personnes, nom_fichier):
    if os.path.exists(nom_fichier):
        with open(nom_fichier, 'r') as fichier_json_lecture:
            try:
                donnees_existantes = json.load(fichier_json_lecture)
            except json.JSONDecodeError:
                donnees_existantes = []
    else:
        donnees_existantes = []

    nouvelles_donnees = [personne.to_dict() for personne in liste_personnes]
    donnees_combinees = donnees_existantes + nouvelles_donnees

    with open(nom_fichier, 'w') as fichier_json_ecriture:
        json.dump(donnees_combinees, fichier_json_ecriture, indent=4)

# Utilisation de la fonction pour sauvegarder
fichier = "personnes.json"
sauvegarder_personnes_json(listes_personne, fichier)

print(f"Une liste de {nombre_de_personnes} personnes a été ajoutée à (ou créée dans) '{fichier}'.")


# Section de test pour ajouter_depense et ajouter_revenu
print("\n--- Test des méthodes ajouter_depense et ajouter_revenu ---")

# Création d'une nouvelle personne pour le test
personne_test = Personne("Doe", "John", "john.doe@example.com", "M", "1985-05-10")

# Création de quelques dépenses de test
depense_test1 = Depense(50, "2025-04-30", "Café")
depense_test2 = Depense(120, "2025-05-01", "Livre")

# Ajout des dépenses à la personne
personne_test.ajouter_depense(depense_test1)
personne_test.ajouter_depense(depense_test2)

# Vérification des dépenses ajoutées
print(f"Nombre de dépenses après ajout : {len(personne_test.depenses)}")
for depense in personne_test.depenses:
    print(f"  - Montant: {depense.montant}, Date: {depense.date}, Description: {depense.description}")

# Création de quelques revenus de test
revenu_test1 = Revenu(100, "2025-04-30", "Pourboire")
revenu_test2 = Revenu(1500, "2025-05-02", "Paie")

# Ajout des revenus à la personne
personne_test.ajouter_revenu(revenu_test1)
personne_test.ajouter_revenu(revenu_test2)

# Vérification des revenus ajoutés
print(f"\nNombre de revenus après ajout : {len(personne_test.revenus)}")
for revenu in personne_test.revenus:
    print(f"  - Montant: {revenu.montant}, Date: {revenu.date}, Description: {revenu.description}")

print("--- Fin du test ---")