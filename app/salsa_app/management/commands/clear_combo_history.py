from django.core.management.base import BaseCommand
from salsa_app.models import ComboHistory

class Command(BaseCommand):
    help = 'Clears the ComboHistory table'

    def handle(self, *args, **options):
        ComboHistory.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully cleared the ComboHistory table'))