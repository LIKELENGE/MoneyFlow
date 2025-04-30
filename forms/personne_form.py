from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email

class PersonneForm(FlaskForm):
    nom = StringField('Nom', validators=[DataRequired()])
    prenom = StringField('Prénom', validators=[DataRequired()])
    mail = StringField('Email', validators=[DataRequired(), Email()])
    sexe = SelectField('Sexe', choices=[('M', 'Homme'), ('F', 'Femme'), ('X', 'Autre')], validators=[DataRequired()])
    date_naissance = DateField('Date de naissance', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Ajouter Personne')