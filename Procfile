release: python manage.py migrate --noinput && python manage.py collectstatic --noinput
web: gunicorn auka_terapias.wsgi --log-file -
