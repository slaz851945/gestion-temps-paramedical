# app/routes/modules.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from app import db
from app.models import Module, Enseignant, Promotion
from app.forms import ModuleForm
from flask_babel import _
from app.decorators import role_required

bp = Blueprint('modules', __name__, url_prefix='/modules')

@bp.route('/')
@login_required
@role_required('admin', 'direction')
def index():
    """Liste des modules."""
    modules = Module.query.all()
    return render_template('modules/index.html', modules=modules)

@bp.route('/ajouter', methods=['GET', 'POST'])
@login_required
@role_required('admin', 'direction')
def ajouter():
    form = ModuleForm()
    if form.validate_on_submit():
        # Gérer les valeurs 0 (aucun) pour les clés étrangères optionnelles
        enseignant_id = form.enseignant_referent_id.data if form.enseignant_referent_id.data != 0 else None
        promotion_id = form.promotion_id.data if form.promotion_id.data != 0 else None
        
        module = Module(
            code=form.code.data,
            intitule=form.intitule.data,
            volume_horaire=form.volume_horaire.data,
            type=form.type.data,
            enseignant_referent_id=enseignant_id,
            promotion_id=promotion_id,
            couleur_affichage=form.couleur_affichage.data,
            description=form.description.data
        )
        db.session.add(module)
        db.session.commit()
        flash(_('Module ajouté avec succès.'), 'success')
        return redirect(url_for('modules.index'))
    return render_template('modules/form.html', form=form, titre=_('Ajouter un module'))

@bp.route('/modifier/<int:id>', methods=['GET', 'POST'])
@login_required
@role_required('admin', 'direction')
def modifier(id):
    module = Module.query.get_or_404(id)
    form = ModuleForm(obj=module)
    if form.validate_on_submit():
        module.code = form.code.data
        module.intitule = form.intitule.data
        module.volume_horaire = form.volume_horaire.data
        module.type = form.type.data
        module.enseignant_referent_id = form.enseignant_referent_id.data if form.enseignant_referent_id.data != 0 else None
        module.promotion_id = form.promotion_id.data if form.promotion_id.data != 0 else None
        module.couleur_affichage = form.couleur_affichage.data
        module.description = form.description.data
        db.session.commit()
        flash(_('Module modifié avec succès.'), 'success')
        return redirect(url_for('modules.index'))
    return render_template('modules/form.html', form=form, titre=_('Modifier un module'))

@bp.route('/supprimer/<int:id>', methods=['POST'])
@login_required
@role_required('admin', 'direction')
def supprimer(id):
    module = Module.query.get_or_404(id)
    db.session.delete(module)
    db.session.commit()
    flash(_('Module supprimé avec succès.'), 'success')
    return redirect(url_for('modules.index'))