# 4. Contraintes techniques et environnement

## 4.1. Architecture générale

Application web architecture client-serveur, accessible via navigateur moderne, responsive (adaptée aux tablettes et smartphones). Multiplateforme.

## 4.2. Stack technologique

| Composant | Technologie / Outil | Justification |
|-----------|---------------------|---------------|
| Back-end | Python 3.10+ | Langage mature, riche en bibliothèques |
| Framework web | Flask (avec extensions) | Léger, flexible, parfait pour un développement modulaire |
| ORM | SQLAlchemy | Abstraction de la base de données |
| Base de données | PostgreSQL 14+ | Robuste, support des contraintes d'intégrité |
| Migrations | Alembic (Flask-Migrate) | Gestion versionnée du schéma |
| Authentification | Flask-Login + Flask-Principal | Gestion des sessions et des rôles |
| Formulaires | Flask-WTF + WTForms | Validation et protection CSRF |
| Tâches asynchrones | Celery + Redis (optionnel V2) | Pour envois d'e-mails et générations lourdes |
| Front-end | HTML5, CSS3, Bootstrap 5 | Interface moderne et responsive |
| Calendrier interactif | FullCalendar | Riche en fonctionnalités, drag & drop, vues multiples |
| Graphiques | Chart.js | Statistiques d'occupation |
| Export PDF | WeasyPrint | Génération à partir de templates HTML/CSS |
| Export Excel | OpenPyXL | Création de fichiers Excel |
| Flux iCal | ics.py | Génération de calendriers synchronisables |
| Serveur web | Nginx + Gunicorn | Mise en production |
| Conteneurisation | **Podman** (avec podman-compose) | Alternative légère et sécurisée à Docker |
| Versionnement | Git (dépôt privé) | Suivi des modifications |

## 4.3. Exigences non fonctionnelles

**Sécurité :**
- Authentification forte (mots de passe hachés avec bcrypt).
- Gestion fine des droits (RBAC) avec contrôle au niveau des vues.
- Protection contre les injections SQL (via ORM), CSRF, XSS.
- Connexions HTTPS obligatoires.
- Journalisation des actions critiques (logs conservés 1 an).

**Performance :**
- Temps de réponse < 2 secondes pour les requêtes courantes.
- Optimisation des requêtes SQL (indexation, jointures).
- Mise en cache (Redis) pour les données peu volatiles (référentiels).

**Disponibilité :** 99,5 % en période d'utilisation courante.

**Maintenabilité :** Code commenté, respect des conventions PEP 8, documentation technique.

**Évolutivité :** Architecture modulaire permettant d'ajouter de nouveaux modules.

**Ergonomie :** Interface intuitive, navigation simple, aides contextuelles.

**Accessibilité :** Respect partiel des normes RGAA.

