release: python manage.py migrate --noinput && python manage.py collectstatic --noinput && python create_superuser.py
web: gunicorn auka_terapias.wsgi --log-file -
