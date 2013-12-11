@ECHO ON
mv ingredients/models.py ingredients/models_tmp.py
mv ingredients/.syncdb.py ingredients/models.py
python manage.py syncdb

type sql_scripts\brands.sql | python manage.py dbshell
type sql_scripts\categories.sql | python manage.py dbshell
type sql_scripts\views.sql | python manage.py dbshell

mv ingredients/models.py ingredients/.syncdb.py
mv ingredients/models_tmp.py ingredients/models.py

python manage.py syncdb