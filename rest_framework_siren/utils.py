
from collections import OrderedDict


def link_maker(rel, href):
    return OrderedDict([
        ('rel', rel),
        ('href', href),
    ])
