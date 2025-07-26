mig:
	python manage.py makemigrations
	python manage.py migrate
admin:
	python manage.py createsuperuser

app:
	python manage.py startapp apps
run:
	python .\manage.py runserver




