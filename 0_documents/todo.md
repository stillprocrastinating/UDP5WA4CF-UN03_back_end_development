# TODO

- "Traffic light" system: difficulty & understanding: "Green" = >75% succeed, "Amber" = >50% succeed, "Red" = <50% succeed of participants, not question answers.


## Deploy

1. Change image references from `0_static` to `1_staticfiles`
1. Remove unused fonts and colours
1. `python manage.py collectstatic`
1. `python manage.py makemigrations`
1. `python manage.py migrate`


## General

- Whenever a package is installed, use `pip freeze > requirements.txt`
- Colours - use https://webaim.org/resources/contrastchecker/
