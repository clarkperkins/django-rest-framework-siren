"""
Siren pagination
"""

from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from rest_framework_siren.utils import link_maker


class SirenPagination(PageNumberPagination):
    """
    Pagination class for Siren
    """

    def get_paginated_response(self, data):
        links = [
            link_maker(['self'], 'self'),
            link_maker(['next'], self.get_next_link()),
            link_maker(['previous'], self.get_previous_link()),
        ]

        return Response(OrderedDict([
            ('properties', {'count': self.page.paginator.count}),
            ('entities', data),
            ('links', links),
        ]))
