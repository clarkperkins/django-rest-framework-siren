"""
Siren pagination
"""

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from rest_framework_siren.compat import OrderedDict


class SirenPagination(PageNumberPagination):
    """
    Pagination class for Siren
    """
    
    def _link_maker(rel, href):
        return OrderedDict(
            ('rel', rel),
            ('href', href),
        )

    def get_paginated_response(self, data):
        links = [
            self._link_maker(['self'], 'self'),
            self._link_maker(['next'], self.get_next_link()),
            self._link_maker(['previous'], self.get_previous_link()),
        ]

        return Response(OrderedDict([
            ('properties', {'count': self.page.paginator.count}),
            ('entities', data),
            ('actions', []),
            ('links', links),
        ]))
