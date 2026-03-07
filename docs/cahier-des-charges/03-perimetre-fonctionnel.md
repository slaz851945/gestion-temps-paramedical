## 3.2. Modules fonctionnels

### 3.2.1. Gestion des référentiels

**Enseignants :**
- Fiche d'identité, coordonnées, spécialités.
- Type : permanent / vacataire.
- Volume horaire maximal par semaine.
- Indisponibilités ponctuelles ou récurrentes (ex: tous les mercredis après-midi, congés) avec support de règles de récurrence (type iCal).

**Salles :**
- Nom, type (cours, TP, amphi, simulation).
- Capacité.
- Équipements spécifiques (vidéoprojecteur, mannequins, tableau blanc, ordinateurs) avec gestion par étiquettes pour faciliter la recherche.

**Groupes :**
- Nom, promotion, effectif.
- Liste des étudiants (import possible depuis Excel, export pour l'appel).

**Modules :**
- Code, intitulé, volume horaire total.
- Type (cours magistral, TD, TP, stage).
- Enseignant référent.
- Prérequis éventuels (liens vers d'autres modules).
- Couleur associée pour l'affichage calendaire (personnalisable).

**Périodes académiques :**
- Année universitaire, semestres, vacances, semaines de stage.
- Gestion des jours fériés.

### 3.2.2. Gestion des contraintes pédagogiques

Ce module permet de définir des règles métier qui seront automatiquement vérifiées lors de la planification :

- **Ordre des modules** : "Le module A doit précéder le module B" (vérification chronologique).
- **Limites horaires** : "Pas de cours après 18h", "Pas plus de 4h consécutives pour un même groupe".
- **Règles spécifiques** : "Un cours de simulation nécessite une salle équipée de mannequins", "L'enseignant X ne peut pas intervenir sur plus de 2 modules différents par jour".
- **Contraintes de stage** : "Pas de cours pendant les périodes de stage", "Un étudiant ne peut pas être en stage et en cours simultanément".

Ces contraintes sont paramétrables et évolutives via une interface dédiée.


### 3.2.3. Planification des cours

**Création/modification/suppression d'une séance :**
- Module concerné.
- Enseignant(s) (possibilité de co-enseignement).
- Groupe(s) concerné(s).
- Salle(s) (possibilité de salles multiples pour les gros groupes).
- Date, heure de début et fin.
- Périodicité (hebdomadaire, bimensuelle) pour les cours réguliers.
- Statut (brouillon, publié, verrouillé).

**Vérification automatique des conflits en temps réel :**
- Disponibilité de la salle.
- Disponibilité de l'enseignant.
- Capacité de la salle >= effectif du groupe.
- Absence de chevauchement avec les périodes de stage des étudiants.
- Respect des contraintes pédagogiques définies.

**Aide intelligente à la recherche de créneaux :**
- Lors de la planification, l'utilisateur sélectionne une date et l'application affiche en temps réel la liste des salles libres ET des enseignants disponibles.
- Filtrage possible par équipement, capacité, type de salle.
- Proposition visuelle des créneaux compatibles (sous forme de grille ou de timeline).

**Workflow de validation :**
- Les plannings passent par différents statuts : **Brouillon** (en cours d'élaboration), **Publié** (visible par tous, notifications envoyées), **Verrouillé** (plus de modification possible, par exemple une semaine avant).
- Historique des modifications accessible.

**Mode simulation ("bac à sable") :**
- Permet à la direction de tester des scénarios ("Et si on décalait les stages de deux semaines ?") sans impacter le planning réel.
- Export possible du scénario simulé pour comparaison.



### 3.2.4. Gestion des examens

**Planification des épreuves :**
- Écrites, orales, pratiques.
- Paramètres spécifiques : durée, nombre de surveillants, matériel nécessaire.
- Gestion multi-salles : possibilité d'affecter plusieurs salles à un même examen (pour les grands groupes).
- Affectation des surveillants (avec vérification de leur disponibilité et respect du nombre requis).

**Gestion des convocations :**
- Génération automatique des convocations individuelles ou par groupe (PDF).
- Envoi par email ou mise à disposition dans l'espace étudiant.

**Tableau de bord des examens :**
- Vue d'ensemble des épreuves à venir.
- Rappels automatiques pour les surveillants et les étudiants (J-7, J-1).




### 3.2.5. Gestion des stages

**Définition des périodes :**
- Périodes de stage par promotion (dates de début et fin).
- Blocage automatique des disponibilités des étudiants pendant ces périodes.

**Suivi des affectations :**
- Interface pour le responsable de stages : validation des conventions, suivi des évaluations.
- Affectation des étudiants dans les structures d'accueil (avec recherche et filtres).

**Contraintes spécifiques :**
- Vérification qu'un étudiant n'est pas planifié en cours pendant son stage.
- Alertes en cas de chevauchement détecté.


### 3.2.6. Visualisation et recherche

**Calendrier interactif :**
- Vues jour, semaine, mois.
- Filtres dynamiques par enseignant, groupe, salle, module, type d'activité.
- Cases colorées par type d'activité (cours, TD, TP, examen, stage).
- Glisser-déposer pour modifier une séance (selon droits).

**Grille de disponibilité des salles :**
- Visualisation des créneaux libres par salle sur une période donnée.
- Recherche rapide d'une salle disponible avec critères (capacité, équipements).

**Emplois du temps individuels :**
- Vue simplifiée pour chaque enseignant et chaque étudiant.
- Export PDF et synchronisation iCal (flux .ics) pour intégration dans les calendriers personnels (Google, Outlook, Apple).

**Tableau de bord des conflits :**
- Liste des conflits non résolus avec niveau de criticité.
- Alertes visuelles pour la direction.


### 3.2.7. Génération de documents

- **Export PDF** d'un emploi du temps (template personnalisable avec logo de l'institut).
- **Export Excel** de la liste des séances pour un module donné.
- **Tableau de surveillance** d'examen : liste des surveillants par salle et par épreuve.
- **Convocations** individuelles ou collectives (PDF).
- **Flux iCal** pour synchronisation externe.
- **Statistiques** : taux d'occupation des salles, charge horaire des enseignants, respect des contraintes.

### 3.2.8. Notifications et alertes

- Envoi d'e-mails automatiques lors de l'affectation/modification d'une séance (avec possibilité de résumé quotidien pour éviter la sur-sollicitation).
- Rappels avant un examen (J-7, J-1) pour les surveillants et les étudiants.
- Alertes en cas de conflit détecté après une modification.
- Notifications de validation (passage en statut "publié" ou "verrouillé").