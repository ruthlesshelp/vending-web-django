# Vending Machine web app in Django

Vending Machine demo website built with the Django framework.

## Mac OS

Use the following command (Mac OS) to create a virtual environment named `.venv` based on your current interpreter:

```zsh
$ python3 -m venv .venv
$ source .venv/bin/activate
```

**NOTE:** Other OS options explained at [Create a project environment for the Django tutorial](https://code.visualstudio.com/docs/python/tutorial-django#_create-a-project-environment-for-the-django-tutorial)

## Install Django

Upgrade `pip`:

```zsh
(.venv) $ python -m pip install --upgrade pip
```

Install Django in the virtual environment by running the following command:

```zsh
(.venv) $ python -m pip install django
```

## SQLite Database

Create an empty development database by running the following command:

```zsh
python manage.py migrate
```
