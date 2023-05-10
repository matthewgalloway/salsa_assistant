from django.core.management.base import BaseCommand
from salsa_app.models import MoveHistory

class Command(BaseCommand):
    help = 'Clears the ComboHistory table'

    def handle(self, *args, **options):
        MoveHistory.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully cleared the MoveHistory table'))