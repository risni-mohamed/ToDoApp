import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo_app.settings")  # replace todo_app
app = get_wsgi_application()
