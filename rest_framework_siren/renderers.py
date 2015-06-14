"""
Provides Siren rendering support.
"""
from __future__ import unicode_literals

from rest_framework.renderers import JSONRenderer


class SirenRenderer(JSONRenderer):
    """
    Renderer which serializes to YAML.
    """

    media_type = 'application/vnd.siren+json'
    format = 'siren'
