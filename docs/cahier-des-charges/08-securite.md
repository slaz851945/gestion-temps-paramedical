# 8. Sécurité et gestion des accès

- **Authentification** : email + mot de passe (avec réinitialisation possible).
- **Autorisations basées sur les rôles** (RBAC) :
  - Administrateur : tout.
  - Direction : création/modification des séances, gestion des groupes, modules, salles, contraintes, consultation de tous les plannings.
  - Responsable stages : gestion des stages, indisponibilités des étudiants, consultation des cours.
  - Enseignant permanent : consultation de son planning, modification de ses indisponibilités, visualisation des groupes/modules dont il a la charge.
  - Enseignant vacataire : consultation de son planning, modification de ses indisponibilités (simplifié).
  - Étudiant : consultation de son planning uniquement.
- Contrôle au niveau des vues pour chaque requête sensible.
- Journalisation des actions critiques (logs conservés 1 an).