import os
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "MakeMigrations and Migrate"

    def handle(self, *args, **kwargs):
        print("Execute MakeMigrations")
        os.system("python manage.py makemigrations")
        print("Execute Migrate")
        os.system("python manage.py migrate")
        print("Start Project")
        os.system("python manage.py runserver 0.0.0.0:8000")
