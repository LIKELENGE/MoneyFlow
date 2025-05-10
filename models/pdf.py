import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

class RapportFinancierPDF:
    def __init__(self, titre, categories, valeurs, couleurs):
        self.titre = titre
        self.categories = categories
        self.valeurs = valeurs
        self.couleurs = couleurs
        self.graph_image = "graphique_camembert.png"
        self.nom_pdf = "rapport_financier.pdf"

    def generer_camembert(self):
        plt.figure(figsize=(5, 5))
        plt.pie(self.valeurs, labels=self.categories, colors=self.couleurs,
                autopct='%1.1f%%', startangle=90)
        plt.title(self.titre)
        plt.axis('equal')
        plt.savefig(self.graph_image)
        plt.close()
        print("Camembert généré.")

    def generer_pdf(self):
        c = canvas.Canvas(self.nom_pdf, pagesize=A4)
        width, height = A4
        c.drawImage(self.graph_image, 100, height - 400, width=300, preserveAspectRatio=True)
        c.setFont("Helvetica", 12)
        c.drawString(100, height - 420, "Répartition mensuelle : revenus et dépenses.")
        c.save()
        print("PDF généré.")

    def creer_rapport(self):
        self.generer_camembert()
        self.generer_pdf()

# --- Utilisation ---
categories = ['Revenus', 'Loyer', 'Nourriture', 'Transport', 'Loisirs']
valeurs = [2700, 900, 500, 300, 300]
couleurs = ['#4CAF50', '#FFC107', '#03A9F4', '#9C27B0', '#F44336']

rapport = RapportFinancierPDF("Répartition des revenus et dépenses", categories, valeurs, couleurs)
rapport.creer_rapport()