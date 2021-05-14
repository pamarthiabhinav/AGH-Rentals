from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = "This Command Let's You Help To List All The Installed Apps In Your Project"

    def handle(self, *args, **options):
        print("Installed Apps:")
        for i in settings.INSTALLED_APPS:
            print(i.capitalize())
