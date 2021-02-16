"""
WSGI config for hansen_brandon_my_first_django_project_assignment project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hansen_brandon_my_first_django_project_assignment.settings')

application = get_wsgi_application()
