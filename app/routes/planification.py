from flask import Blueprint, render_template

bp = Blueprint('planification', __name__)

@bp.route('/planification')
def index():
    return render_template('index.html')