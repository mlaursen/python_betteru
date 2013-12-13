@ECHO ON
cd ingredients
rename models.py models_tmp.py
rename .syncdb.py models.py
cd ..

python manage.py syncdb
type sql_scripts\procedures.sql | python manage.py dbshell
type sql_scripts\brands.sql | python manage.py dbshell
type sql_scripts\categories.sql | python manage.py dbshell

cd ingredients
rename models.py .syncdb.py
rename models_tmp.py models.py
cd ..

type sql_scripts\accounts.sql | python manage.py dbshell
type sql_scripts\ingredients.sql | python manage.py dbshell
type sql_scripts\meals.sql | python manage.py dbshell
type sql_scripts\mealparts.sql | python manage.py dbshell
type sql_scripts\views.sql | python manage.py dbshell

python manage.py syncdb
