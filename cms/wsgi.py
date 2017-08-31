"""
WSGI config for cms project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

from __future__ import absolute_import, unicode_literals

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cms.settings.dev")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
