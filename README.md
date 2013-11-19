dj-dynamic-forms
================

Dynamic forms for Django

**dj-dynamic-forms** lets you create your forms through the Django admin.
You can add and remove form fields as you need them. That makes it perfect
for creating survey or application forms.

It uses `Postgres Hstore` extension to store forms data.

This project is fork of [django-dynamic-forms](https://github.com/Markush2010/django-dynamic-forms) by [Markush2010](https://github.com/Markush2010) mainly to use Postgres Hstore by default.


## Install
```
1. pip install -r requirements.txt
2. pip install dynamic_forms
```
Postgres extension `Hstore` must be installed manually.
 
```
CREATE EXTENSION Hstore;
```

## Usage


Add ``'dynamic_forms'`` to the ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'dynamic_forms',
        ...
    )

Add ``'dynamic_forms.middlewares.FormModelMiddleware'`` to the
``MIDDLEWARE_CLASSES`` (probably at the end)::

    MIDDLEWARE_CLASSES = (
        ...
        'dynamic_forms.middlewares.FormModelMiddleware'
    )

You can set ``DYNAMIC_FORMS_EMAIL_RECIPIENTS`` in your settings to a list of
e-mail addresses. Forms being send via e-mail will then be send to those
addresses instead of those defined in ``settings.ADMINS``. Each recipient will
see *all* other recipients. See [send_mail](https://docs.djangoproject.com/en/stable/topics/email/#django.core.mail.send_mail)
in the officiall documentation.


## Example

1. Change into the ``example/`` directory
2. Run ``./manage.py runserver``

The *admin* is available at http://127.0.0.1:8000/admin/.

* Username: ``admin``
* Password: ``password``

You can find an example form at http://127.0.0.1:8000/example-form/.


## Running the tests

1. Change into the ``tests/`` directory
2. Run ``./runtests.sh``

