# app/utils.py
# Fonctions utilitaires pour l'application.
# On utilise Werkzeug pour le hachage sécurisé des mots de passe.

from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password):
    """
    Génère un hash sécurisé à partir d'un mot de passe en clair.
    Utilise l'algorithme par défaut de Werkzeug (scrypt ou pbkdf2 selon la version).
    """
    return generate_password_hash(password)

def verify_password(password_hash, password):
    """
    Vérifie si un mot de passe en clair correspond à son hash.
    Retourne True si la correspondance est correcte, False sinon.
    """
    return check_password_hash(password_hash, password)