# create_admin.py
from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

app = create_app()
with app.app_context():
    # Vérifier si l'utilisateur existe déjà
    user = User.query.filter_by(email="admin@gestiontemps.com").first()
    if user:
        # Mettre à jour le mot de passe si l'utilisateur existe
        user.password_hash = generate_password_hash("admin")
        print("Mot de passe de l'admin mis à jour.")
    else:
        # Créer un nouvel administrateur
        admin = User(
            email="admin@gestiontemps.com",
            prenom="Admin",
            nom="Super",
            role="admin",
            password_hash=generate_password_hash("admin")
        )
        db.session.add(admin)
        print("Administrateur créé.")
    db.session.commit()
    print("Opération terminée.")