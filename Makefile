install-poetry:
	pip install poetry

install-deps:
    poetry install

test:
	poetry run python manage.py test

makemigrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

run:
	poetry run python manage.py runserver
