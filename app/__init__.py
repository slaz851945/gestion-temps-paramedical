"""
Module d'initialisation de l'application Flask.
Configure les extensions, les blueprints et le contexte d'exécution.
"""

from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_babel import Babel, lazy_gettext as _l
from flask_migrate import Migrate  # <-- NOUVEAU
from app.config import Config

# Initialisation des extensions
db = SQLAlchemy()
migrate = Migrate()  # <-- NOUVEAU
login_manager = LoginManager()
csrf = CSRFProtect()
babel = Babel()

def get_locale():
    """
    Sélectionne la langue de l'interface.
    Priorité : session > en-tête Accept-Language > français par défaut.
    """
    if 'language' in session:
        return session['language']
    return request.accept_languages.best_match(['fr', 'ar_DZ']) or 'fr'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Désactive le cache des templates (utile en développement)
    app.jinja_env.cache = {}

    # Initialisation des extensions avec l'application
    db.init_app(app)
    migrate.init_app(app, db)  # <-- NOUVEAU
    login_manager.init_app(app)
    csrf.init_app(app)

    # Initialisation de Babel (sans l'argument configure_jinja)
    # babel.init_app(app, locale_selector=get_locale, configure_jinja=True)
    babel.init_app(app, locale_selector=get_locale)

    # Configuration de Flask-Login
    login_manager.login_view = 'auth.login'
    login_manager.login_message = _l("Veuillez vous connecter pour accéder à cette page.")
    login_manager.login_message_category = "info"

    # Callback pour charger un utilisateur
    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return User.query.get(int(user_id))

    # Contexte processor pour injecter la langue courante dans les templates
    @app.context_processor
    def inject_language():
        return dict(current_language=get_locale(), get_locale=get_locale)

    # Enregistrement des blueprints
    from app.routes import main, auth, planification
    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(planification.bp)

    from app.routes import enseignants
    app.register_blueprint(enseignants.bp)

    from app.routes import salles
    app.register_blueprint(salles.bp)

    from app.routes import groupes
    app.register_blueprint(groupes.bp)

    from app.routes import modules
    app.register_blueprint(modules.bp)

    from app.routes import promotions
    app.register_blueprint(promotions.bp)

    

    # Gestionnaire d'erreur 403
    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/403.html'), 403

    return app

