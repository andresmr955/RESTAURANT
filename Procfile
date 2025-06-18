release: python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn productivity_restaurant.wsgi:application --bind 0.0.0.0:$PORT
