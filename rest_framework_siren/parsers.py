"""
Provides Siren parsing support.
"""
from __future__ import unicode_literals

from rest_framework.parsers import JSONParser

from rest_framework_siren import renderers


class SirenParser(JSONParser):
    """
    Sets the media type for siren.
    """

    media_type = 'application/vnd.siren+json'
    renderer_class = renderers.SirenRenderer
