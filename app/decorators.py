# app/decorators.py
"""
Décorateurs personnalisés pour la gestion des rôles et permissions.
"""

from functools import wraps
from flask import flash, redirect, url_for, abort, request
from flask_login import current_user
from flask_babel import _  # pour les messages traduisibles

def role_required(*roles):
    """
    Décorateur pour restreindre l'accès à une vue en fonction du rôle de l'utilisateur.
    
    Utilisation : @role_required('admin', 'direction')
    
    Si l'utilisateur n'est pas connecté, il est redirigé vers la page de connexion.
    Si l'utilisateur est connecté mais n'a pas le rôle requis, une erreur 403 (Forbidden) est levée.
    """
    def decorator(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
                # L'utilisateur n'est pas connecté -> redirection vers login
                flash(_("Veuillez vous connecter pour accéder à cette page."), "warning")
                return redirect(url_for('auth.login', next=request.url))
            if current_user.role not in roles:
                # L'utilisateur n'a pas le bon rôle -> accès interdit
                abort(403)  # Page "Forbidden"
            return func(*args, **kwargs)
        return decorated_view
    return decorator