# 10. Méthodologie de gestion de projet

Le développement suivra une approche itérative et incrémentale (type Agile) avec des sprints de 2 à 3 semaines. Cette méthodologie permet une livraison progressive des fonctionnalités, une adaptation continue aux retours et une maîtrise des risques.

## Phases du projet

1. **Cadrage, conception détaillée et maquettage UI/UX** (3 semaines) :
   - Validation du cahier des charges.
   - Maquettage des écrans principaux (wireframes puis mockups).
   - Tests utilisateurs sur prototypes.
   - Choix techniques définitifs.

2. **Mise en place de l'environnement** (1 semaine) :
   - Dépôt Git, structure du projet.
   - Base de données, conteneurisation Podman, intégration continue.

3. **Développement itératif (6 sprints)** (15 semaines) :
   - Sprint 1 : Authentification, gestion des rôles, CRUD des référentiels de base.
   - Sprint 2 : Module de planification simplifiée (calendrier, création de séances, détection basique de conflits).
   - Sprint 3 : Gestion des examens et des stages.
   - Sprint 4 : Moteur de contraintes pédagogiques et workflow de validation.
   - Sprint 5 : Génération de documents (PDF, Excel, iCal) et notifications.
   - Sprint 6 : Finalisation, optimisation, tests avancés.

4. **Tests et recette** (3 semaines) :
   - Tests unitaires et fonctionnels.
   - Recette utilisateur avec jeu de données réel.
   - Corrections et ajustements.

5. **Formation et déploiement** (2 semaines) :
   - Formation des super-utilisateurs.
   - Documentation utilisateur.
   - Déploiement pilote puis généralisé avec Podman.

**Total estimé : 24 semaines (environ 6 mois)**.

## Livraison et suivi

- Chaque sprint donne lieu à une démonstration des fonctionnalités développées.
- Un tableau de bord (type Trello ou GitHub Projects) suit l'avancement des user stories.
- Les spécifications détaillées et les comptes rendus de réunion sont conservés dans le dossier `docs/`.