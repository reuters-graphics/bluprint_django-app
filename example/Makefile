export PIPENV_VENV_IN_PROJECT=1

bootstrap:
	pipenv install --dev
	pipenv run python manage.py migrate


superuser:
	pipenv run python manage.py createsuperuser


migrations:
	pipenv run python manage.py makemigrations


develop:
	pipenv run python manage.py migrate
	pipenv run python manage.py runserver