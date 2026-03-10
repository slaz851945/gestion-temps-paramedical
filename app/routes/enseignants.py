# app/routes/enseignants.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from app import db
from app.models import User, Enseignant
from app.forms import EnseignantForm
from flask_babel import _
from app.decorators import role_required  # à créer

from app.utils import hash_password


bp = Blueprint('enseignants', __name__, url_prefix='/enseignants')

@bp.route('/')
@login_required
@role_required('admin', 'direction')
def index():
    """Liste des enseignants."""
    enseignants = Enseignant.query.all()
    return render_template('enseignants/index.html', enseignants=enseignants)

@bp.route('/ajouter', methods=['GET', 'POST'])
@login_required
@role_required('admin', 'direction')
def ajouter():
    form = EnseignantForm()
    if form.validate_on_submit():
        # Créer d'abord l'utilisateur avec le rôle enseignant
        user = User(
            email=form.email.data,
            prenom=form.prenom.data,
            nom=form.nom.data,
            role='enseignant_permanent' if form.type.data == 'permanent' else 'enseignant_vacataire'
        )
        user.password_hash = hash_password('motdepasseprovisoire')  # Mot de passe provisoire
        db.session.add(user)
        db.session.flush()  # Pour obtenir l'ID user

        enseignant = Enseignant(
            user_id=user.id,
            specialites=form.specialites.data,
            max_heures_semaine=form.max_heures_semaine.data,
            telephone=form.telephone.data,
            type=form.type.data
        )
        db.session.add(enseignant)
        db.session.commit()
        flash(_('Enseignant ajouté avec succès.'), 'success')
        return redirect(url_for('enseignants.index'))
    return render_template('enseignants/form.html', form=form, titre=_('Ajouter un enseignant'))


@bp.route('/modifier/<int:id>', methods=['GET', 'POST'])
@login_required
@role_required('admin', 'direction')
def modifier(id):
    enseignant = Enseignant.query.get_or_404(id)
    form = EnseignantForm()
    if form.validate_on_submit():
        # Mise à jour
        enseignant.user.email = form.email.data
        enseignant.user.prenom = form.prenom.data
        enseignant.user.nom = form.nom.data
        enseignant.specialites = form.specialites.data
        enseignant.max_heures_semaine = form.max_heures_semaine.data
        enseignant.telephone = form.telephone.data
        enseignant.type = form.type.data
        db.session.commit()
        flash(_('Enseignant modifié avec succès.'), 'success')
        return redirect(url_for('enseignants.index'))
    # Pré-remplir le formulaire pour l'affichage GET
    form.email.data = enseignant.user.email
    form.prenom.data = enseignant.user.prenom
    form.nom.data = enseignant.user.nom
    form.specialites.data = enseignant.specialites
    form.max_heures_semaine.data = enseignant.max_heures_semaine
    form.telephone.data = enseignant.telephone
    form.type.data = enseignant.type
    return render_template('enseignants/form.html', form=form, titre=_('Modifier un enseignant'))

# @bp.route('/modifier/<int:id>', methods=['GET', 'POST'])
# @login_required
# @role_required('admin', 'direction')
# def modifier(id):
#     enseignant = Enseignant.query.get_or_404(id)
#     form = EnseignantForm(obj=enseignant.user)  # pré-remplit les champs user
#     if form.validate_on_submit():
#         # Mise à jour de l'utilisateur
#         enseignant.user.email = form.email.data
#         enseignant.user.prenom = form.prenom.data
#         enseignant.user.nom = form.nom.data
#         # Mise à jour de l'enseignant
#         enseignant.specialites = form.specialites.data
#         enseignant.max_heures_semaine = form.max_heures_semaine.data
#         enseignant.telephone = form.telephone.data
#         enseignant.type = form.type.data
#         db.session.commit()
#         flash(_('Enseignant modifié avec succès.'), 'success')
#         return redirect(url_for('enseignants.index'))
#     # Pré-remplir les champs spécifiques à l'enseignant pour l'affichage initial
#     form.specialites.data = enseignant.specialites
#     form.max_heures_semaine.data = enseignant.max_heures_semaine
#     form.telephone.data = enseignant.telephone
#     form.type.data = enseignant.type
#     return render_template('enseignants/form.html', form=form, titre=_('Modifier un enseignant'))


@bp.route('/supprimer/<int:id>', methods=['POST'])
@login_required
@role_required('admin', 'direction')
def supprimer(id):
    enseignant = Enseignant.query.get_or_404(id)
    user = enseignant.user
    db.session.delete(enseignant)
    db.session.delete(user)  # Supprime également l'utilisateur associé
    db.session.commit()
    flash(_('Enseignant supprimé avec succès.'), 'success')
    return redirect(url_for('enseignants.index'))