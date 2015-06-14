
from rest_framework_siren.compat import OrderedDict


def link_maker(rel, href):
    return OrderedDict([
        ('rel', rel),
        ('href', href),
    ])
