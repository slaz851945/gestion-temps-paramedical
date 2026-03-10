# Guide des opérations CRUD

## Structure générale
Chaque référentiel (enseignants, salles, groupes, promotions, modules) suit le même pattern :
- Modèle SQLAlchemy dans `app/models.py`
- Formulaire WTForms dans `app/forms.py`
- Routes dans un blueprint dédié (`app/routes/xxx.py`)
- Templates dans `app/templates/xxx/`

## Protection
Toutes les routes sont protégées par `@login_required` et `@role_required('admin', 'direction')`.

## Traductions
Les libellés sont marqués avec `_()` dans les templates et `_l()` dans les formulaires. Les catalogues de traduction sont dans `translations/`.