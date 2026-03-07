# 7. Exigences d'interface utilisateur et d'expérience (UI/UX)

L'application devra offrir une expérience utilisateur (UX) fluide, intuitive et efficace, et une interface utilisateur (UI) moderne, claire et cohérente. L'objectif est de minimiser la courbe d'apprentissage et de maximiser la productivité des utilisateurs, quel que soit leur rôle ou leur aisance avec les outils numériques.

## 7.1. Principes généraux d'ergonomie

- **Simplicité et clarté :** L'interface doit être épurée, sans éléments superflus. Chaque écran doit avoir un objectif unique et clair. La hiérarchie visuelle (titres, sections, boutons) doit guider naturellement l'utilisateur.
- **Cohérence :** Les éléments d'interface (boutons, icônes, formulaires, couleurs) doivent être utilisés de manière cohérente dans toute l'application. Un bouton "Ajouter" aura toujours la même apparence et la même position relative.
- **Feedback immédiat :** Chaque action de l'utilisateur (clic, soumission de formulaire, glisser-déposer) doit donner lieu à un retour visuel ou textuel immédiat :
    - Animation de chargement pour les actions longues.
    - Message de confirmation (vert) ou d'erreur (rouge) clairement visible après une soumission.
    - Mise en évidence d'un élément lors du survol (hover).
- **Prévention et gestion des erreurs :**
    - Autant que possible, l'interface doit empêcher l'utilisateur de commettre une erreur (ex : désactiver un bouton "Enregistrer" tant que le formulaire n'est pas valide).
    - Les messages d'erreur doivent être **explicites, en français courant**, et indiquer comment corriger le problème ("Le format de l'email est incorrect" plutôt que "Erreur 400").
- **Guidage et aide contextuelle :**
    - Des infobulles (tooltips) doivent expliquer les icônes ou les champs de formulaire complexes.
    - Un lien "Aide" ou un point d'interrogation peut ouvrir une aide contextuelle sur la page en cours.
- **Raccourcis et productivité :**
    - Pour les utilisateurs fréquents (direction, responsable de stages), des raccourcis clavier seront implémentés pour les actions courantes (ex: `Ctrl+N` pour nouvelle séance, `Ctrl+S` pour enregistrer).
    - Le glisser-déposer (drag & drop) sera privilégié pour la planification dans le calendrier (sous réserve des droits).
- **Accessibilité :** L'interface doit respecter les critères de base du RGAA (Référentiel Général d'Amélioration de l'Accessibilité) : contrastes suffisants, navigation au clavier possible, textes alternatifs pour les images.

## 7.2. Exigences spécifiques par module

### 7.2.1. Dashboard (Tableau de bord)

- **Vue d'ensemble personnalisée :** Chaque rôle doit voir un dashboard adapté. Par exemple :
    - **Direction :** Alertes de conflits, taux d'occupation des salles, prochains examens, liste des plannings en attente de validation.
    - **Enseignant :** Prochains cours, notifications de changements, rappels de saisie d'indisponibilités.
    - **Étudiant :** Emploi du temps du jour et du lendemain, prochain examen, période de stage en cours ou à venir.
- **Widgets interactifs :** Les informations clés doivent être présentées sous forme de widgets que l'utilisateur peut potentiellement réorganiser (option à étudier en V2). Les graphiques (Chart.js) doivent être simples et lisibles.

### 7.2.2. Calendrier (FullCalendar)

C'est le cœur de l'application. Son interface est cruciale.

- **Vues multiples et fluides :** Passage instantané entre les vues "jour", "semaine", "mois". Le chargement des événements doit être fluide, sans rechargement complet de la page (utilisation d'AJAX).
- **Code couleur intuitif :** Chaque type d'activité (CM, TD, TP, Examen, Stage) et/ou chaque module doit avoir une couleur dédiée, définie dans la gestion des modules. Les couleurs doivent être suffisamment contrastées et distinguables.
- **Informations contextuelles :** Le survol d'un événement dans le calendrier doit afficher une infobulle avec les détails essentiels (module, salle, enseignant, groupe).
- **Clic et glisser-déposer :**
    - Clic simple sur un événement : ouvre la fiche de détail (en lecture seule ou modification selon droits).
    - Glisser-déposer d'un événement : permet de le déplacer rapidement. Une vérification instantanée des conflits doit s'opérer pendant le déplacement (la case devient rouge en cas de conflit, verte si OK).
    - Redimensionnement d'un événement : en tirant le bord inférieur, on modifie la durée du cours.
- **Filtres dynamiques et instantanés :** Une barre de filtres (par enseignant, groupe, salle, module) doit permettre de filtrer les événements affichés **en temps réel**, sans rechargement. Les filtres doivent être sous forme de "pills" (pastilles) que l'on active/désactive.
- **Recherche de créneaux (fonction "Aide à la planification") :**
    - Lors de la création d'une séance, l'utilisateur choisit une date cible.
    - L'application affiche, sous le formulaire ou dans un panneau latéral, la **grille de disponibilité** des salles pour cette date, avec mise en évidence des créneaux où la salle ET l'enseignant (si déjà sélectionné) sont libres.
    - Un clic sur un créneau libre pré-remplit automatiquement les champs "date", "heure début" et "heure fin" du formulaire.

### 7.2.3. Formulaires (création/modification)

- **Simplicité et progressivité :** Les formulaires longs doivent être découpés en étapes ou sections claires.
- **Validation en temps réel :** La vérification des conflits doit se faire au fur et à mesure du remplissage, pas seulement à la soumission. Par exemple, dès que l'utilisateur sélectionne un enseignant et une salle, une icône (✓ vert ou ✗ rouge) peut indiquer la compatibilité.
- **Saisie intelligente :**
    - Champs de recherche avec autocomplétion pour les enseignants, modules, salles (éviter les longues listes déroulantes).
    - Pour les cours récurrents, un pattern de saisie simple (type "tous les lundis du [date] au [date]").
- **Responsive design :** Les formulaires doivent être parfaitement utilisables sur mobile (champs en colonne, boutons de taille adaptée).

### 7.2.4. Emplois du temps personnels (vues Enseignant/Étudiant)

- **Concentration sur l'essentiel :** La vue doit être simplifiée au maximum, sans les contrôles de gestion complexes réservés à la direction.
- **Export en un clic :** Boutons d'export bien visibles vers PDF et vers le flux iCal (avec une icône de calendrier standard).
- **Synchronisation externe :** Le flux iCal doit être accessible via une URL unique que l'utilisateur peut copier-coller dans son application de calendrier. Un QR code peut même être généré pour faciliter la configuration sur mobile.

## 7.3. Performance perçue (Fluidité)

- **Temps de chargement initial :** Le premier chargement de l'application doit être inférieur à 3 secondes sur une connexion standard.
- **Temps de réponse aux interactions :** Les actions courantes (clic, filtre, soumission) doivent donner un retour en moins d'une seconde. Pour les actions plus longues (génération d'un gros PDF), un indicateur de progression avec estimation du temps restant doit être affiché.
- **"Single Page Application" (SPA) légère :** L'utilisation d'AJAX et de composants dynamiques (via JavaScript vanilla ou Stimulus.js, par exemple) permettra d'éviter les rechargements de page intempestifs, donnant une sensation d'application de bureau.

## 7.4. Design et identité visuelle

- **Charte graphique :** L'interface devra respecter la charte graphique de l'institut (couleurs, logo, typographie). Une maquette précise (fournie par l'institut ou co-construite avec le prestataire) sera la référence.
- **Police de caractères :** Utilisation d'une police moderne, lisible et accessible (ex: Open Sans, Lato, ou la police institutionnelle).
- **Icônes :** Utilisation d'une bibliothèque d'icônes cohérente et reconnaissable (ex: Font Awesome ou Heroicons).

## 7.5. Méthodologie de conception et de validation UI/UX

1. **Phase de maquettage (Wireframes) :** Avant tout développement, des maquettes fonctionnelles (wireframes) seront réalisées pour valider les parcours utilisateurs et l'organisation des écrans.
2. **Phase de design (Mockups) :** Une fois les wireframes validés, des maquettes graphiques haute-fidélité (mockups) seront produites pour valider le look & feel final.
3. **Tests utilisateurs :** Des tests d'utilisabilité seront organisés avec des représentants de chaque rôle (direction, enseignant, étudiant) sur les maquettes interactives (prototypes cliquables) avant le début du développement.
4. **Revue itérative :** Pendant le développement, chaque fonctionnalité livrée fera l'objet d'une revue par le porteur de projet pour s'assurer de sa conformité avec les attentes UI/UX.