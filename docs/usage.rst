=====
Usage
=====

To use Django Uploads App in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_uploads_app.apps.DjangoUploadsAppConfig',
        ...
    )

Add Django Uploads App's URL patterns:

.. code-block:: python

    from django_uploads_app import urls as django_uploads_app_urls


    urlpatterns = [
        ...
        url(r'^', include(django_uploads_app_urls)),
        ...
    ]
