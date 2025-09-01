import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_app.settings')  # Change 'todo_app' to your project folder name
application = get_wsgi_application()
