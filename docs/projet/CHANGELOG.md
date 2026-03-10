# Changelog

# Changelog

## [0.3.0] - 2026-03-10
### Ajouté
- CRUD complet pour les enseignants
- CRUD complet pour les salles
- CRUD complet pour les promotions
- CRUD complet pour les groupes
- CRUD complet pour les modules
- Internationalisation avec Flask-Babel (français et arabe algérien)
- Gestion des rôles avec décorateur `@role_required`
- Flask-Migrate pour la gestion des migrations de base de données

### Modifié
- Correction des erreurs de templates (blocs title, balises mal fermées)
- Correction des traductions dans les fichiers `.po`
- Amélioration de la navigation (liens conditionnels selon le rôle)

### Sécurité
- Protection des routes CRUD par rôle (admin/direction uniquement)

<!-- 
## [Unreleased]
### Ajouté
- Mise en place de l'internationalisation (Flask-Babel)
- Marquage des textes dans les templates et les formulaires
- Configuration des langues française et arabe

### Modifié
- Adaptation des routes pour gérer la langue
- ...

## [0.1.0] - 2026-03-08
- Structure initiale du projet
- Authentification basique -->