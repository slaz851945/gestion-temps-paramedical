# app/routes/promotions.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from app import db
from app.models import Promotion
from app.forms import PromotionForm
from flask_babel import _
from app.decorators import role_required

bp = Blueprint('promotions', __name__, url_prefix='/promotions')

@bp.route('/')
@login_required
@role_required('admin', 'direction')
def index():
    """Liste des promotions."""
    promotions = Promotion.query.order_by(Promotion.annee_debut.desc()).all()
    return render_template('promotions/index.html', promotions=promotions)

@bp.route('/ajouter', methods=['GET', 'POST'])
@login_required
@role_required('admin', 'direction')
def ajouter():
    form = PromotionForm()
    if form.validate_on_submit():
        promotion = Promotion(
            nom=form.nom.data,
            annee_debut=form.annee_debut.data,
            annee_fin=form.annee_fin.data
        )
        db.session.add(promotion)
        db.session.commit()
        flash(_('Promotion ajoutée avec succès.'), 'success')
        return redirect(url_for('promotions.index'))
    return render_template('promotions/form.html', form=form, titre=_('Ajouter une promotion'))

@bp.route('/modifier/<int:id>', methods=['GET', 'POST'])
@login_required
@role_required('admin', 'direction')
def modifier(id):
    promotion = Promotion.query.get_or_404(id)
    form = PromotionForm(obj=promotion)
    if form.validate_on_submit():
        promotion.nom = form.nom.data
        promotion.annee_debut = form.annee_debut.data
        promotion.annee_fin = form.annee_fin.data
        db.session.commit()
        flash(_('Promotion modifiée avec succès.'), 'success')
        return redirect(url_for('promotions.index'))
    return render_template('promotions/form.html', form=form, titre=_('Modifier une promotion'))

@bp.route('/supprimer/<int:id>', methods=['POST'])
@login_required
@role_required('admin', 'direction')
def supprimer(id):
    promotion = Promotion.query.get_or_404(id)
    # Vérifier si des groupes ou modules sont liés à cette promotion
    if promotion.groupes.count() > 0 or promotion.modules.count() > 0:
        flash(_('Impossible de supprimer cette promotion car elle est liée à des groupes ou modules.'), 'danger')
        return redirect(url_for('promotions.index'))
    db.session.delete(promotion)
    db.session.commit()
    flash(_('Promotion supprimée avec succès.'), 'success')
    return redirect(url_for('promotions.index'))