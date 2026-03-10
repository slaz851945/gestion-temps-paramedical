# app/forms.py
# Ce module définit les formulaires WTForms utilisés dans l'application.
# WTForms assure la validation des données côté serveur et la protection CSRF.

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, Optional, NumberRange, EqualTo, ValidationError
from flask_babel import lazy_gettext as _l
from app.models import User  # pour la validation d'email unique


class RegistrationForm(FlaskForm):
    """
    Formulaire d'inscription d'un nouvel utilisateur.
    Tous les champs sont obligatoires.
    """
    # Champ email avec validation d'email et longueur max
    email = StringField('Email', validators=[
        DataRequired(message="L'email est obligatoire."),
        Email(message="Format d'email invalide."),
        Length(max=120, message="L'email ne doit pas dépasser 120 caractères.")
    ])
    
    # Champ prénom
    prenom = StringField('Prénom', validators=[
        DataRequired(message="Le prénom est obligatoire."),
        Length(max=80, message="Le prénom ne doit pas dépasser 80 caractères.")
    ])
    
    # Champ nom
    nom = StringField('Nom', validators=[
        DataRequired(message="Le nom est obligatoire."),
        Length(max=80, message="Le nom ne doit pas dépasser 80 caractères.")
    ])
    
    # Champ mot de passe (avec confirmation)
    password = PasswordField('Mot de passe', validators=[
        DataRequired(message="Le mot de passe est obligatoire."),
        Length(min=6, message="Le mot de passe doit contenir au moins 6 caractères.")
    ])
    confirm_password = PasswordField('Confirmer le mot de passe', validators=[
        DataRequired(message="Veuillez confirmer le mot de passe."),
        EqualTo('password', message="Les mots de passe ne correspondent pas.")
    ])
    
    # Rôle (choix parmi une liste prédéfinie)
    role = SelectField('Rôle', choices=[
        ('etudiant', 'Étudiant'),
        ('enseignant_vacataire', 'Enseignant vacataire'),
        ('enseignant_permanent', 'Enseignant permanent')
    ], validators=[DataRequired(message="Le rôle est obligatoire.")])
    
    submit = SubmitField('S\'inscrire')

    def validate_email(self, email):
        """
        Validation personnalisée : vérifie que l'email n'est pas déjà utilisé.
        Cette méthode est automatiquement appelée par WTForms.
        """
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Cet email est déjà associé à un compte. Veuillez en choisir un autre.')


class LoginForm(FlaskForm):
    """
    Formulaire de connexion.
    """
    email = StringField('Email', validators=[
        DataRequired(message="L'email est obligatoire."),
        Email(message="Format d'email invalide.")
    ])
    password = PasswordField('Mot de passe', validators=[
        DataRequired(message="Le mot de passe est obligatoire.")
    ])
    submit = SubmitField('Se connecter')



# app/forms.py (ajout)

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Optional, NumberRange, Length

class EnseignantForm(FlaskForm):
    # Champs hérités de User (à pré-remplir si modification)
    email = StringField(_l('Email'), validators=[DataRequired(), Email(), Length(max=120)])
    prenom = StringField(_l('Prénom'), validators=[DataRequired(), Length(max=80)])
    nom = StringField(_l('Nom'), validators=[DataRequired(), Length(max=80)])

    # Champs spécifiques à Enseignant
    specialites = StringField(_l('Spécialités'), validators=[Optional(), Length(max=200)],
                              description=_l('Séparer les spécialités par des virgules'))
    max_heures_semaine = IntegerField(_l('Volume horaire max/semaine'), 
                                      validators=[Optional(), NumberRange(min=1, max=40)],
                                      default=20)
    telephone = StringField(_l('Téléphone'), validators=[Optional(), Length(max=20)])
    type = SelectField(_l('Type'), choices=[('permanent', 'Permanent'), ('vacataire', 'Vacataire')],
                       validators=[DataRequired()])

    submit = SubmitField(_l('Enregistrer'))


    # app/forms.py (ajout)

class SalleForm(FlaskForm):
    nom = StringField(_l('Nom'), validators=[DataRequired(), Length(max=50)])
    type = SelectField(_l('Type'), choices=[
        ('cours', _l('Cours')),
        ('tp', _l('TP')),
        ('amphi', _l('Amphithéâtre')),
        ('simulation', _l('Simulation'))
    ], validators=[DataRequired()])
    capacite = IntegerField(_l('Capacité'), validators=[DataRequired(), NumberRange(min=1, max=500)])
    equipements = StringField(_l('Équipements'), validators=[Optional(), Length(max=200)],
                              description=_l('Séparer les équipements par des virgules'))
    submit = SubmitField(_l('Enregistrer'))



# app/forms.py (ajout)

from app.models import Promotion  # si vous utilisez Promotion

class GroupeForm(FlaskForm):
    nom = StringField(_l('Nom du groupe'), validators=[DataRequired(), Length(max=50)])
    promotion = SelectField(_l('Promotion'), coerce=int, validators=[DataRequired()])
    effectif = IntegerField(_l('Effectif'), validators=[DataRequired(), NumberRange(min=0, max=500)])
    submit = SubmitField(_l('Enregistrer'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.promotion.choices = [(p.id, p.nom) for p in Promotion.query.order_by(Promotion.nom).all()]



# app/forms.py (ajout)

from app.models import Enseignant, Promotion

class ModuleForm(FlaskForm):
    code = StringField(_l('Code'), validators=[DataRequired(), Length(max=20)])
    intitule = StringField(_l('Intitulé'), validators=[DataRequired(), Length(max=200)])
    volume_horaire = IntegerField(_l('Volume horaire'), validators=[DataRequired(), NumberRange(min=1, max=500)])
    type = SelectField(_l('Type'), choices=[
        ('cours', _l('Cours')),
        ('td', _l('TD')),
        ('tp', _l('TP')),
        ('stage', _l('Stage'))
    ], validators=[DataRequired()])
    enseignant_referent_id = SelectField(_l('Enseignant référent'), coerce=int, validators=[Optional()])
    promotion_id = SelectField(_l('Promotion'), coerce=int, validators=[Optional()])
    couleur_affichage = StringField(_l('Couleur'), validators=[Optional(), Length(max=7)],
                                    default="#3788d8", render_kw={"type": "color"})
    description = TextAreaField(_l('Description'), validators=[Optional(), Length(max=500)])
    submit = SubmitField(_l('Enregistrer'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remplir les listes déroulantes avec les données de la base
        self.enseignant_referent_id.choices = [(0, _l('-- Aucun --'))] + [
            (e.id, f"{e.user.prenom} {e.user.nom}") for e in Enseignant.query.order_by(Enseignant.user_id).all()
        ]
        self.promotion_id.choices = [(0, _l('-- Aucune --'))] + [
            (p.id, p.nom) for p in Promotion.query.order_by(Promotion.nom).all()
        ]


# app/forms.py (ajout)

class PromotionForm(FlaskForm):
    nom = StringField(_l('Nom de la promotion'), validators=[DataRequired(), Length(max=50)])
    annee_debut = IntegerField(_l('Année de début'), validators=[Optional(), NumberRange(min=2000, max=2100)])
    annee_fin = IntegerField(_l('Année de fin'), validators=[Optional(), NumberRange(min=2000, max=2100)])
    submit = SubmitField(_l('Enregistrer'))

    def validate(self, **kwargs):
        # Validation personnalisée : si année début et fin sont fournies, fin > début
        if not super().validate(**kwargs):
            return False
        if self.annee_debut.data and self.annee_fin.data and self.annee_fin.data <= self.annee_debut.data:
            self.annee_fin.errors.append(_('L\'année de fin doit être supérieure à l\'année de début.'))
            return False
        return True