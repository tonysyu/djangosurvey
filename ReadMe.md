Django App Tutorial
===================

This is my first Django app based on the [official
tutorial](https://docs.djangoproject.com/en/1.10/intro/tutorial01/).


Installation
------------

This tutorial was created using Python 3.6. To install dependencies, run:

    $ pip install -r requrements.txt

If you don't have a working Python install (or this project isn't working on
your normal install), you can install [Anaconda](https://www.continuum.io/downloads) and run

    $ conda create -n djangosurveyenv python=3.6
    $ source activate djangosurveyenv

After installing dependencies, you'll need to follow the database-update
instructions below to initialize the database.


Database updates
----------------

When updating models for this app, make sure to run the following to update
the schema:

    $ python manage.py makemigrations polls
    $ python manage.py migrate

The first command creates the migrations for changes to models.py. The second
applies those migrations.

To explore the database, you can run:

    $ sqlite3 db.sqlite3
    sqlite> .tables


Testing and conventions
-----------------------

Any committed code should pass all tests, which are run with

    $ python manage.py test

Also, all committed code should pass basic PEP8 and linting requirements,
which is verified using:

    $ flake8

Since this is not needed for the actual app, you'll have to run the following
to install dev requirements:

    $ pip install -r dev-requrements.txt


Notes to myself
---------------

My super user is `tyu` and I used an old default password.


To Do
-----

- Tests
    - Add test suite for ResultsView
    - Exclude questions without choices (in view, maybe elsewhere)
        - Also assert question with choice(s) is published
    - Try Django's LiveServerTestCase
    - Integrate coverage.py
    - Check out [Testing in Django](https://docs.djangoproject.com/en/1.10/topics/testing/)
