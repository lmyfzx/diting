# -*- coding: utf-8 -*-
#
from django.conf import settings

def diting_processor(request):
    context = {}

    # Setting default pk
    context.update(
        {'DEFAULT_PK': '00000000-0000-0000-0000-000000000000', 'dt_settings': settings}
    )
    return context



