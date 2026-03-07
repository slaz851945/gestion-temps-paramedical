# 5. Modèle de données (principales entités)

**users** : id, email, password_hash, role (admin, direction, resp_stage, enseignant_permanent, enseignant_vacataire, etudiant), nom, prenom, actif, dernière_connexion…

**enseignants** (hérite de users ou table liée) : spécialités, max_heures_semaine, telephone, type (permanent/vacataire)

**etudiants** : id, numero_etudiant, groupe_id, …

**groupes** : id, nom, promotion_id, effectif

**promotions** : id, nom, annee_debut, annee_fin

**salles** : id, nom, type, capacite, equipements (table JSON ou table dédiée equipements)

**modules** : id, code, intitule, volume_horaire, type, enseignant_referent_id, promotion_id, couleur_affichage

**contraintes_pedagogiques** : id, type_contrainte, parametres (JSON), actif

**seances** : id, module_id, type_seance (cours, TD, TP, examen), date, heure_debut, heure_fin, statut (brouillon, publie, verrouille), salle_principale_id

**seances_salles** (pour salles multiples) : seance_id, salle_id

**seances_enseignants** : seance_id, enseignant_id, role (principal, surveillant, etc.)

**seances_groupes** : seance_id, groupe_id

**examens** (hérite de seances) : duree, nb_surveillants_requis, consignes

**stages** : id, etudiant_id, structure_id, date_debut, date_fin, tuteur, statut

**indisponibilites** : id, enseignant_id, date_debut, date_fin, recurrent (règle iCal), motif

**logs_actions** : id, user_id, action, table_concernee, enregistrement_id, timestamp, details (JSON)