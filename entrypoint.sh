#!/bin/bash

poetry run python manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
poetry run python manage.py migrate