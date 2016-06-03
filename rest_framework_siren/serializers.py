"""
Serializers for Siren
"""

import logging

from rest_framework.serializers import *
from rest_framework.settings import api_settings

from rest_framework_siren.utils import link_maker

logger = logging.getLogger(__name__)


class SirenSerializerMixin(object):
    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        model_cls = self.Meta.model
        return_class = '%s.%s' % (model_cls._meta.app_label, model_cls._meta.model_name)

        properties = OrderedDict()
        entities = []
        links = []

        fields = [field for field in self.fields.values() if not field.write_only]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if attribute is None:
                # We skip `to_representation` for `None` values so that
                # fields do not have to explicitly deal with that case.
                properties[field.field_name] = None
            else:
                value = field.to_representation(attribute)

                # The order matters here - if they are switched, links end up in the wrong places
                if field.field_name == api_settings.URL_FIELD_NAME:
                    links.append(link_maker(['self'], value))
                elif isinstance(field, HyperlinkedIdentityField):
                    entities.append(link_maker([field.field_name], value))
                elif isinstance(field, HyperlinkedRelatedField):
                    links.append(link_maker([field.field_name], value))
                else:
                    properties[field.field_name] = value

        return OrderedDict([
            ('class', return_class),
            ('properties', properties),
            ('entities', entities),
            ('links', links),
        ])


class ModelSerializer(SirenSerializerMixin, ModelSerializer):
    pass


class HyperlinkedModelSerializer(SirenSerializerMixin, HyperlinkedModelSerializer):
    pass
