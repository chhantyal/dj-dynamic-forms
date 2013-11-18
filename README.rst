===================
Django Dynamic Form
===================

.. image:: https://pypip.in/v/django-dynamic-forms/badge.png
   :target: https://crate.io/packages/django-dynamic-forms/

.. image:: https://pypip.in/d/django-dynamic-forms/badge.png
   :target: https://crate.io/packages/django-dynamic-forms/

.. image:: https://travis-ci.org/Markush2010/django-dynamic-forms.png
   :target: https://travis-ci.org/Markush2010/django-dynamic-forms

.. image:: https://coveralls.io/repos/Markush2010/django-dynamic-forms/badge.png?branch=develop
   :target: https://coveralls.io/r/Markush2010/django-dynamic-forms


**django-dynamic-forms** lets you create your forms through the Django admin.
You can add and remove form fields as you need them. That makes it perfect
for creating survey or application forms.


INSTALLATION
============

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
see *all* other recipients. See `send_mail
<https://docs.djangoproject.com/en/stable/topics/email/#django.core.mail.send_mail>`_
in the officiall documentation.


Example
=======

1. Change into the ``example/`` directory
2. Run ``./manage.py runserver``

The *admin* is available at http://127.0.0.1:8000/admin/.

* Username: ``admin``
* Password: ``password``

You can find an example form at http://127.0.0.1:8000/example-form/.


Running the tests
=================

1. Change into the ``tests/`` directory
2. Run ``./runtests.sh``
