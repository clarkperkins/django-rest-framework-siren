# REST Framework Siren

[![build-status-image]][travis]
[![pypi-version]][pypi]

**Siren hypermedia support for Django REST Framework**


## Overview

Siren hypermedia support extracted as a third party package directly from the official Django REST Framework implementation. It's based on the Siren specification located [https://github.com/kevinswiber/siren][here].

## Requirements

* Python (2.7, 3.3, 3.4)
* Django (1.6, 1.7, 1.8)
* Django REST Framework (2.4+, 3.0+)

## Installation

Install using `pip`...

```bash
$ pip install djangorestframework-siren
```

## Example

```python
REST_FRAMEWORK = {
    # Optional - will simply set the media type to application/vnd.siren+json
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework_siren.renderers.SirenRenderer',
    ),
    
    # Also optional - will allow responses with a application/vnd.siren+json media type
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework_siren.parsers.SirenParser',
    ),
    
    # Required - 
    'DEFAULT_PAGINATION_CLASS': 'rest_framework_siren.pagination.SirenPagination',
}
```

You must then use the serializers defined in the `rest_framework_siren.serizlizers` module.  
There is currently only support for the `ModelSerizlizer` and `HyperlinkedModelSerializer` types.

For example, if this is your current `serializers.py` file:
```python
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
```

Simply swap out the serializers import to use `rest_framework_siren` instead of `rest_framework`:
```python
# Use rest_framework_siren instead
from rest_framework_siren import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
```


You can also set the renderer, parser, and paginator used for an individual view, or viewset, using the APIView class based views.

```python
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
```




### Sample output

```json
{
  "class": "auth.user",
  "properties": {
    "email": "clarkperkins@example.com",
    "is_staff": true,
    "username": "clarkperkins"
  },
  "links": [
    "rel": ["self"], "href": "http://127.0.0.1:8000/users/1/"
  ]
}
```

## Documentation & Support

Full documentation for the project is available at [http://clarkperkins.github.io/django-rest-framework-siren][docs].

You may also want to follow the [author][clarkperkins] on Twitter.


[build-status-image]: https://secure.travis-ci.org/clarkperkins/django-rest-framework-siren.svg?branch=master
[travis]: http://travis-ci.org/clarkperkins/django-rest-framework-siren?branch=master
[pypi-version]: https://img.shields.io/pypi/v/djangorestframework-siren.svg
[pypi]: https://pypi.python.org/pypi/djangorestframework-siren
[docs]: http://clarkperkins.github.io/django-rest-framework-siren
[clarkperkins]: https://twitter.com/rclarkperkins