=======================
django-telegram-objects
=======================

.. image:: https://img.shields.io/github/workflow/status/ramiboutas/django-telegram-objects/CI/master?style=for-the-badge
   :target: https://github.com/ramiboutas/django-telegram-objects/actions?workflow=CI

.. image:: https://img.shields.io/badge/Coverage-100%25-success?style=for-the-badge
  :target: https://github.com/ramiboutas/django-telegram-objects/actions?workflow=CI

.. image:: https://img.shields.io/pypi/v/django-telegram-objects.svg?style=for-the-badge
    :target: https://pypi.org/project/django-telegram-objects/

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
    :target: https://github.com/psf/black

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit



About
-----

A Django App that creates Telegram objects of a bot in a Postgres Database.
The bot has to have permission to read the messages of the Chat objects where is the member of.


Requirements
------------

Python 3.7 to 3.11 supported.

Django 3.2 to 4.1 supported.


----

Setup
-----

Install from **pip**:

.. code-block:: sh

    python -m pip install django-telegram-objects

Add it to your installed apps:

.. code-block:: python

    INSTALLED_APPS = [
        ...,
        "telegram_objects",
        ...,
    ]


Make sure you are using a Postgres database and migrate the tables:

.. code-block:: sh

    python manage.py migrate



Set up
------

In you project settings:

Add your bot token: ``TELEGRAM_BOT_API_KEY``

Recommendation: save your bot token a .env file

.. code-block:: text

    TELEGRAM_BOT_API_KEY=<your-token>


Load your secrets keys and tokens using,
for example, [python-dotenv](https://pypi.org/project/python-dotenv/)
and access to the key using ``os.environ.get`` method:

.. code-block:: python

    TELEGRAM_BOT_API_KEY = os.environ.get("TELEGRAM_BOT_API_KEY")


Add models you would like to see in your Django admin:

Example:

.. code-block:: python

    TELEGRAM_MODELS_IN_ADMIN_SITE = (
        "Chat",
        "Message",
        "Document",
    )


How to use
----------

Once the app is set up, you can get updates by running the command:

.. code-block:: sh

    python manage.py get_updates
