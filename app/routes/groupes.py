# app/routes/groupes.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from app import db
from app.models import Groupe, Promotion
from app.forms import GroupeForm
from flask_babel import _
from app.decorators import role_required

bp = Blueprint('groupes', __name__, url_prefix='/groupes')

@bp.route('/')
@login_required
@role_required('admin', 'direction')
def index():
    """Liste des groupes."""
    groupes = Groupe.query.all()
    return render_template('groupes/index.html', groupes=groupes)

@bp.route('/ajouter', methods=['GET', 'POST'])
@login_required
@role_required('admin', 'direction')
def ajouter():
    form = GroupeForm()
    if form.validate_on_submit():
        groupe = Groupe(
            nom=form.nom.data,
            promotion_id=form.promotion.data,
            effectif=form.effectif.data
        )
        db.session.add(groupe)
        db.session.commit()
        flash(_('Groupe ajouté avec succès.'), 'success')
        return redirect(url_for('groupes.index'))
    print("Titre passé au template:", _('Ajouter un groupe'))
    return render_template('groupes/form.html', form=form, titre=_('Ajouter un groupe'))



@bp.route('/modifier/<int:id>', methods=['GET', 'POST'])
@login_required
@role_required('admin', 'direction')
def modifier(id):
    groupe = Groupe.query.get_or_404(id)
    form = GroupeForm(obj=groupe)
    if form.validate_on_submit():
        groupe.nom = form.nom.data
        groupe.promotion_id = form.promotion.data
        groupe.effectif = form.effectif.data
        db.session.commit()
        flash(_('Groupe modifié avec succès.'), 'success')
        return redirect(url_for('groupes.index'))
    return render_template('groupes/form.html', form=form, titre=_('Modifier un groupe'))

@bp.route('/supprimer/<int:id>', methods=['POST'])
@login_required
@role_required('admin', 'direction')
def supprimer(id):
    groupe = Groupe.query.get_or_404(id)
    db.session.delete(groupe)
    db.session.commit()
    flash(_('Groupe supprimé avec succès.'), 'success')
    return redirect(url_for('groupes.index'))