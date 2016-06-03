REST Framework Siren
====================

|TravisCI| |PyPi|

**Siren hypermedia support for Django REST Framework**

Overview
--------

Siren hypermedia support extracted as a third party package directly
from the official Django REST Framework implementation. It's based on
the Siren specification located
`here <https://github.com/kevinswiber/siren>`__.

*Note:* As of the 0.1.0 release, ``django-rest-framework-siren`` does
not support adding ``actions`` as specified by siren.

Requirements
------------

-  Python (2.7, 3.4)
-  Django (1.7, 1.8, 1.9)
-  Django REST Framework (2.4+, 3.0+)

Installation
------------

Install using ``pip``...

.. code:: bash

    $ pip install djangorestframework-siren

Example
-------

.. code:: python

    REST_FRAMEWORK = {
        # Optional - will simply set the media type to application/vnd.siren+json
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework_siren.renderers.SirenRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
            ...
        ),
        
        # Also optional - will allow responses with a application/vnd.siren+json media type
        'DEFAULT_PARSER_CLASSES': (
            'rest_framework_siren.parsers.SirenParser',
            ...
        ),
        
        # Required - does the transformation into siren formatting
        'DEFAULT_PAGINATION_CLASS': 'rest_framework_siren.pagination.SirenPagination',
    }

| You must then use the serializers defined in the ``rest_framework_siren.serializers`` module.
| There is currently support for the ``Serializer``, ``ModelSerializer`` and ``HyperlinkedModelSerializer`` types.


For example, if this is your current ``serializers.py`` file:

.. code:: python

    from rest_framework import serializers

    class UserSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = User
            fields = ('url', 'username', 'email', 'is_staff')

Simply swap out the serializers import to use ``rest_framework_siren``
instead of ``rest_framework``:

.. code:: python

    # Use rest_framework_siren instead
    from rest_framework_siren import serializers

    class UserSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = User
            fields = ('url', 'username', 'email', 'is_staff')

You can also set the renderer, parser, and paginator used for an
individual view, or viewset, using the APIView class based views.

.. code:: python

    from rest_framework import routers, viewsets
    from rest_framework_siren import serializers  # NOTE - using rest_framework_siren.serializers
    from rest_framework_siren.parsers import SirenParser
    from rest_framework_siren.renderers import SirenRenderer
    from rest_framework_siren.pagination import SirenPagination

    # Serializers define the API representation.
    class UserSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = User
            fields = ('url', 'username', 'email', 'is_staff')


    # ViewSets define the view behavior.
    class UserViewSet(viewsets.ModelViewSet):
        queryset = User.objects.all()
        serializer_class = UserSerializer
        parser_classes = (SirenParser,)
        renderer_classes = (SirenRenderer,)
        pagination_class = SirenPagination

Sample output
~~~~~~~~~~~~~

.. code:: json

    {
      "class": "auth.user",
      "properties": {
        "email": "clarkperkins@example.com",
        "is_staff": true,
        "username": "clarkperkins"
      },
      "links": [
        {"rel": ["self"], "href": "http://127.0.0.1:8000/users/1/"}
      ]
    }

Documentation & Support
-----------------------

Full documentation for the project is available at https://djangorestframework-siren.readthedocs.io/en/latest/.

You may also want to follow the `author <https://twitter.com/rclarkperkins>`__ on Twitter.

.. |TravisCI| image:: https://travis-ci.org/clarkperkins/django-rest-framework-siren.svg?branch=master
   :target: https://travis-ci.org/clarkperkins/django-rest-framework-siren
.. |PyPi| image:: https://img.shields.io/pypi/v/djangorestframework-siren.svg
   :target: https://pypi.python.org/pypi/djangorestframework-siren
