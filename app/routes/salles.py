
# app/routes/salles.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from app import db
from app.models import Salle
from app.forms import SalleForm
from flask_babel import _
from app.decorators import role_required
import json

bp = Blueprint('salles', __name__, url_prefix='/salles')

@bp.route('/')
@login_required
@role_required('admin', 'direction')
def index():
    """Liste des salles."""
    salles = Salle.query.all()
    return render_template('salles/index.html', salles=salles)

@bp.route('/ajouter', methods=['GET', 'POST'])
@login_required
@role_required('admin', 'direction')
def ajouter():
    form = SalleForm()
    if form.validate_on_submit():
        # Convertir la chaîne d'équipements en liste JSON
        equipements_list = [e.strip() for e in form.equipements.data.split(',')] if form.equipements.data else []
        salle = Salle(
            nom=form.nom.data,
            type=form.type.data,
            capacite=form.capacite.data,
            equipements=json.dumps(equipements_list)  # Stocker comme JSON
        )
        db.session.add(salle)
        db.session.commit()
        flash(_('Salle ajoutée avec succès.'), 'success')
        return redirect(url_for('salles.index'))
    return render_template('salles/form.html', form=form, titre=_('Ajouter une salle'))

@bp.route('/modifier/<int:id>', methods=['GET', 'POST'])
@login_required
@role_required('admin', 'direction')
def modifier(id):
    salle = Salle.query.get_or_404(id)
    form = SalleForm(obj=salle)
    if form.validate_on_submit():
        salle.nom = form.nom.data
        salle.type = form.type.data
        salle.capacite = form.capacite.data
        equipements_list = [e.strip() for e in form.equipements.data.split(',')] if form.equipements.data else []
        salle.equipements = json.dumps(equipements_list)
        db.session.commit()
        flash(_('Salle modifiée avec succès.'), 'success')
        return redirect(url_for('salles.index'))
    # Pré-remplir le champ équipements à partir du JSON
    if salle.equipements:
        form.equipements.data = ', '.join(json.loads(salle.equipements))
    return render_template('salles/form.html', form=form, titre=_('Modifier une salle'))

@bp.route('/supprimer/<int:id>', methods=['POST'])
@login_required
@role_required('admin', 'direction')
def supprimer(id):
    salle = Salle.query.get_or_404(id)
    db.session.delete(salle)
    db.session.commit()
    flash(_('Salle supprimée avec succès.'), 'success')
    return redirect(url_for('salles.index'))
