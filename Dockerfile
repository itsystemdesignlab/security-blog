# base image
FROM python:3.10-slim as python-base
ENV DockerHOME=/home/app/webapp

# set work directory
RUN mkdir -p $DockerHOME

# where your code lives
WORKDIR $DockerHOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install poetry

# copy whole project to your docker home directory.
COPY . $DockerHOME
COPY pyproject.toml poetry.lock $DockerHOME
# run this command to install all dependencies
RUN poetry install --no-root
# give permission to entrypoint.sh
# port where the Django app runs
EXPOSE 8000

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]