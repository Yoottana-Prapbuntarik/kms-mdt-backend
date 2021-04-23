web: gunicorn backend.wsgi --log-file -

release: python manage.py collectstatic && python manage.py makemigrations  && python manage.py migrate
