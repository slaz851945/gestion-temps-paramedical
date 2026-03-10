# app/models.py
# Ce fichier contient les modèles de données SQLAlchemy pour l'application.

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

# Note: L'extension SQLAlchemy est initialisée dans __init__.py,
# nous l'importons depuis l'application pour éviter les imports circulaires.
from app import db

class User(UserMixin, db.Model):
    """
    Modèle représentant un utilisateur de l'application.
    Hérite de UserMixin pour fournir les méthodes requises par Flask-Login
    (is_authenticated, is_active, is_anonymous, get_id()).
    """
    __tablename__ = 'users'  # Nom de la table dans la base de données

    # Colonnes de la table
    id = db.Column(db.Integer, primary_key=True)  # Identifiant unique auto-incrémenté
    email = db.Column(db.String(120), unique=True, nullable=False)  # Email unique, obligatoire
    password_hash = db.Column(db.String(128), nullable=False)  # Hash du mot de passe (ne stocke jamais le mot de passe en clair)
    nom = db.Column(db.String(80), nullable=False)  # Nom de famille
    prenom = db.Column(db.String(80), nullable=False)  # Prénom
    role = db.Column(db.String(20), nullable=False, default='etudiant')
    # Rôle possible : 'admin', 'direction', 'resp_stage', 'enseignant_permanent', 'enseignant_vacataire', 'etudiant'
    
    actif = db.Column(db.Boolean, default=True)  # Si le compte est actif (désactivé plutôt que supprimé)
    derniere_connexion = db.Column(db.DateTime, nullable=True)  # Date de dernière connexion (peut être nulle)
    
    # Relations (à compléter plus tard avec d'autres tables)
    # Par exemple, un enseignant aura des indisponibilités, etc.

    def __repr__(self):
        """Représentation lisible de l'objet pour le débogage."""
        return f"<User {self.email} ({self.role})>"

    def get_id(self):
        """
        Surcharge de get_id pour retourner l'identifiant sous forme de chaîne.
        Nécessaire pour Flask-Login.
        """
        return str(self.id)

    # Propriétés pour Flask-Login (déjà fournies par UserMixin, mais on peut les surcharger si besoin)
    # @property
    # def is_active(self):
    #     return self.actif


    # app/models.py (à ajouter)

class Enseignant(db.Model):
    """Informations complémentaires pour les utilisateurs ayant le rôle enseignant."""
    __tablename__ = 'enseignants'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
    specialites = db.Column(db.String(200))  # Liste de spécialités (séparées par des virgules)
    max_heures_semaine = db.Column(db.Integer, default=20)
    telephone = db.Column(db.String(20))
    type = db.Column(db.String(20), default='permanent')  # 'permanent' ou 'vacataire'

    # Relation avec User
    user = db.relationship('User', backref=db.backref('enseignant', uselist=False))



# app/models.py (à ajouter)

class Salle(db.Model):
    """Modèle représentant une salle (cours, TP, amphi, simulation)."""
    __tablename__ = 'salles'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), unique=True, nullable=False)
    type = db.Column(db.String(20), nullable=False)  # 'cours', 'tp', 'amphi', 'simulation'
    capacite = db.Column(db.Integer, nullable=False)
    equipements = db.Column(db.JSON)  # Stocke une liste d'équipements en JSON

    def __repr__(self):
        return f"<Salle {self.nom} ({self.type}, {self.capacite} places)>"


# app/models.py (à ajouter)

class Groupe(db.Model):
    """Modèle représentant un groupe d'étudiants."""
    __tablename__ = 'groupes'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), unique=True, nullable=False)
    promotion_id = db.Column(db.Integer, db.ForeignKey('promotions.id'), nullable=False)
    effectif = db.Column(db.Integer, nullable=False, default=0)

    # Relation avec Promotion (à créer si besoin)
    promotion = db.relationship('Promotion', backref='groupes')

    def __repr__(self):
        return f"<Groupe {self.nom} (promo {self.promotion.nom})>"


# app/models.py (à ajouter)

class Module(db.Model):
    """Modèle représentant un module d'enseignement."""
    __tablename__ = 'modules'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False)  # Code unique du module (ex: "MED101")
    intitule = db.Column(db.String(200), nullable=False)  # Intitulé du module
    volume_horaire = db.Column(db.Integer, nullable=False)  # Volume horaire total
    type = db.Column(db.String(20), nullable=False)  # 'cours', 'td', 'tp', 'stage'
    enseignant_referent_id = db.Column(db.Integer, db.ForeignKey('enseignants.id'), nullable=True)
    promotion_id = db.Column(db.Integer, db.ForeignKey('promotions.id'), nullable=True)
    couleur_affichage = db.Column(db.String(7), default="#3788d8")  # Code couleur hexadécimal pour le calendrier
    description = db.Column(db.Text, nullable=True)  # Description optionnelle

    # Relations
    enseignant_referent = db.relationship('Enseignant', backref='modules_referent')
    promotion = db.relationship('Promotion', backref='modules')

    def __repr__(self):
        return f"<Module {self.code} - {self.intitule}>"



class Promotion(db.Model):
    """Promotion (année scolaire)."""
    __tablename__ = 'promotions'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), unique=True, nullable=False)  # ex: "2025-2026"
    annee_debut = db.Column(db.Integer)
    annee_fin = db.Column(db.Integer)

    def __repr__(self):
        return f"<Promotion {self.nom}>"



