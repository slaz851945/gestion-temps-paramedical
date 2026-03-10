"""
Configuration de l'application.
Utilise les variables d'environnement (via python-dotenv) avec des valeurs par défaut.
"""

import os
from dotenv import load_dotenv

load_dotenv()  # Charge les variables d'un fichier .env si présent

class Config:
    """
    Configuration de base de l'application.
    Les classes filles peuvent surcharger pour différents environnements.
    """

    # Clé secrète pour les sessions et la sécurité
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'une-cle-secrete-par-defaut-a-changer-en-production'

    # Base de données
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # --- Configuration de l'internationalisation (i18n) ---
    # Langues supportées par l'application
    LANGUAGES = ['fr', 'ar_DZ']

    # Langue par défaut
    BABEL_DEFAULT_LOCALE = 'fr'

    # Dossier contenant les traductions (chemin absolu)
    # On construit le chemin absolu vers le dossier 'translations' à la racine du projet
    basedir = os.path.abspath(os.path.dirname(__file__))          # dossier app/
    BABEL_TRANSLATION_DIRECTORIES = os.path.join(basedir, '..', 'translations')


