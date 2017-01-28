Django Survey App
=================

Django survey app based on the [official
tutorial](https://docs.djangoproject.com/en/1.10/intro/tutorial01/). Instead of
the default sqlite database, this uses a MySQL database.


Installation
------------

Install MySQL
.............

- [Download MySQL](https://dev.mysql.com/downloads/mysql/) and follow
  [installation instructions](https://dev.mysql.com/doc/refman/5.7/en/installing.html).

- Add the following to your bash profile:

    export PATH="/usr/local/mysql/bin:$PATH"

Initialize Database and User
............................

Start a MySQL interactive session and create the database and user needed for
this project:

    $ mysql -u root -p
    mysql> CREATE USER djangouser@localhost IDENTIFIED BY 'replace-this-password';
    mysql> CREATE DATABASE djangosurvey CHARACTER SET UTF8;
    mysql> CREATE DATABASE test_djangosurvey CHARACTER SET UTF8;
    mysql> GRANT ALL PRIVILEGES ON djangosurvey.* TO djangouser@localhost;
    mysql> GRANT ALL PRIVILEGES ON test_djangosurvey.* TO djangouser@localhost;
    mysql> FLUSH PRIVILEGES;
    mysql> exit

You'll also want to run export your password so that the Django app can access
the database:

    export DJANGOUSER_MYSQL_PASSWORD=replace-this-password

In the code-blocks above, you should *replace `replace-this-password` with an
actual password*.

Finally, you'll need to follow the database-update instructions below to initialize the database schema.

Install Python and dependencies
...............................

This tutorial was created using Python 3.6.  If you don't have a working Python
install (or this project isn't working on your normal install), you can install
[Anaconda](https://www.continuum.io/downloads) and run

    $ conda create -n djangosurvey-env python=3.6
    $ source activate djangosurvey-env

To install dependencies, run:

    $ pip install -r requrements.txt


Database updates
----------------

When updating models for this app, make sure to run the following to update
the schema:

    $ python manage.py makemigrations polls
    $ python manage.py migrate

The first command creates the migrations for changes to models.py. The second
applies those migrations.


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


To Do
-----

- Tests
    - Add test suite for ResultsView
    - Exclude questions without choices (in view, maybe elsewhere)
        - Also assert question with choice(s) is published
    - Try Django's LiveServerTestCase
    - Integrate coverage.py
    - Check out [Testing in Django](https://docs.djangoproject.com/en/1.10/topics/testing/)
