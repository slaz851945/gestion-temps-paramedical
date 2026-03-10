# creer_admin.py (à placer à la racine du projet)
from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

app = create_app()
with app.app_context():

    admin = User.query.filter_by(role="admin").first()  # ou filtrez par email si vous le connaissez
    if admin:
        admin.email = "admin@gestiontemps.com"
        admin.password_hash = generate_password_hash("admin")
        db.session.commit()
        print("Compte admin mis à jour.")
    else:
        print("Aucun administrateur trouvé.")