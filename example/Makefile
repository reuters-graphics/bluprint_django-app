export PIPENV_VENV_IN_PROJECT=1

env:
	pipenv install --dev
	pipenv run python manage.py migrate


superuser:
	pipenv run python manage.py createsuperuser


migrations:
	pipenv run python manage.py makemigrations


app:
	pipenv run python manage.py migrate
	pipenv run python manage.py runserver