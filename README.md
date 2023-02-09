# Django App


> This is my django app. This structure is legit structure.

## Contents
- [Setup](#setup)
  - [Setup with Docket](#docker)
- [Docs](#docs)
- [Third-Party Packages](#third-party-packages)
  - [Poetry](#poetry)
  - [django](#django)
  - [django-debug-toolbar](#django-debug-toolbar)
  - [django-crispy-forms](#django-crispy-forms)
  - [black](#black)
  - [isort](#isort)
  - [sphinx](#sphinx)
- [Tests](#tests)

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/karatas/sample-django-app.git
$ cd sample-django-app
```

Create a virtual environment to install dependencies in and activate it. Then install the dependencies::

```sh
$ poetry install
$ poetry shell
```
For run application:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
## Docker
You can build application and run easily like that.
```sh
$ docker-compose up --build
```
And navigate to `http://0.0.0.1:8000/`.
## Third-Party Packages
_ All used third party packages from me.

### Packages List
- [poetry](https://github.com/python-poetry/poetry) - Package manager.
- [django](https://github.com/django/django) - Python web development framework.
- [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar) - Django debug toolbar.
- [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms) - Django forms. It can be easily integrated
- [django-summernote](https://github.com/summernote/django-summernote) - Summernote is a simple WYSIWYG editor.
django-summernote allows you to embed Summernote into Django very handy. Support admin mixins and widgets.
- [black](https://github.com/psf/black) - Black is the uncompromising Python code formatter.
- [isort](https://github.com/PyCQA/isort) - isort is a Python utility / library to sort imports alphabetically, and automatically separated into sections and by type.
- [sphinx](https://github.com/sphinx-doc/sphinx) - Sphinx uses reStructuredText as its markup language, and many of its strengths come from the power and straightforwardness of reStructuredText and its parsing and translating suite, the Docutils..
- 

### Docs
Go to docs/ folder.
```sh
$ (env) make html
```
And sphinx generates .rst formaat to html. Visit `_build/html` under docs.

### Tests
```sh
$ (env) python manage.py test
```




