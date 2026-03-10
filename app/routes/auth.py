# app/routes/auth.py
# Blueprint pour toutes les routes liées à l'authentification.
# Contient les pages d'inscription, de connexion et de déconnexion.

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, logout_user, login_required
from app import db
from app.models import User
from app.forms import RegistrationForm, LoginForm
from app.utils import hash_password, verify_password

# Création du blueprint pour l'authentification
bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    Page d'inscription.
    Si l'utilisateur est déjà connecté, on le redirige vers l'accueil.
    """
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        # Les données du formulaire sont valides
        # Création d'un nouvel utilisateur
        user = User(
            email=form.email.data,
            prenom=form.prenom.data,
            nom=form.nom.data,
            role=form.role.data,
            password_hash=hash_password(form.password.data)  # On hash le mot de passe
        )
        # Ajout à la base de données
        db.session.add(user)
        db.session.commit()
        
        flash('Votre compte a été créé avec succès ! Vous pouvez maintenant vous connecter.', 'success')
        return redirect(url_for('auth.login'))
    
    # Si le formulaire n'est pas validé (première visite ou erreurs), on affiche le template
    return render_template('auth/register.html', title='Inscription', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    Page de connexion.
    Si l'utilisateur est déjà connecté, redirection vers l'accueil.
    """
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        # Recherche de l'utilisateur par email
        user = User.query.filter_by(email=form.email.data).first()
        
        # Vérification : utilisateur existe ET mot de passe correct
        if user and verify_password(user.password_hash, form.password.data):
            # Connexion réussie
            login_user(user, remember=False)  # 'remember' pourrait être ajouté via une case à cocher
            # Redirection vers la page demandée initialement (s'il y en a une)
            next_page = request.args.get('next')
            flash(f'Bonjour {user.prenom}, vous êtes connecté.', 'success')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            # Échec de connexion
            flash('Email ou mot de passe incorrect.', 'danger')
    
    return render_template('auth/login.html', title='Connexion', form=form)


@bp.route('/logout')
@login_required  # Cette route nécessite d'être connecté
def logout():
    """
    Déconnexion de l'utilisateur.
    """
    logout_user()
    flash('Vous avez été déconnecté.', 'info')
    return redirect(url_for('main.index'))