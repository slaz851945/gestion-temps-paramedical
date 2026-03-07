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