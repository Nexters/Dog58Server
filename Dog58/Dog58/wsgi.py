"""
WSGI config for Dog58 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# sys.path.append("/home/todaytrend/www/todaytrend/Dog58")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Dog58.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
