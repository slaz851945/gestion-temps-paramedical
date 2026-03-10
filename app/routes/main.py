"""
Blueprint pour les routes principales (accueil, changement de langue, etc.)
"""

from flask import Blueprint, render_template, session, redirect, url_for, request, flash, current_app
from flask_babel import _

# Création du blueprint
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """Page d'accueil publique."""
    from flask_babel import gettext
    # Debug console : doit afficher la traduction selon la langue active
    print(gettext('Gestion du temps'))
    return render_template('index.html')

@bp.route('/set-language/<lang>')
def set_language(lang):
    """
    Change la langue de l'interface et redirige vers la page précédente.
    La langue choisie est stockée en session.
    """
    supported = current_app.config.get('LANGUAGES', ['fr', 'ar_DZ'])


    if lang in supported:
        session['language'] = lang
        flash(_('Langue changée avec succès.'), 'success')
    else:
        flash(_('Langue non supportée.'), 'danger')

    print(f"Changement de langue vers : {lang}")
    return redirect(request.referrer or url_for('main.index'))


# app/routes/main.py (ajout à la fin)
from app.decorators import role_required

@bp.route('/admin')
@role_required('admin')
def admin_dashboard():
    """
    Tableau de bord réservé aux administrateurs.
    """
    return render_template('admin/dashboard.html')

