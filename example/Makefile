bootstrap:
	pipenv install --dev
	pipenv run python manage.py migrate
	pipenv run python manage.py createsuperuser

develop:
	pipenv run python manage.py migrate
	pipenv run python manage.py runserver