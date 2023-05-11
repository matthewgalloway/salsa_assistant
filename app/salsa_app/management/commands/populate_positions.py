from django.core.management.base import BaseCommand
from salsa_app.models import Position, Move

BASE_MOVES = [
    "CrossBody-InsideTurn",
    "CrossBody-OutsideTurn",
    "CrossBody",
    "InsideTurn",
    "OutsideTurn",
    "Leader hammerlock",
    "Follower hammerlock",
    "Copa",
    "OpenBreak",
    "Titanic",
    "RightSidePass",
    "BodyWrap",
]

class Command(BaseCommand):
    help = "Populates positions in the database."

    def handle(self, *args, **options):
        # Create positions
        for move_name in BASE_MOVES:
            position, created = Position.objects.get_or_create(name=move_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created position '{move_name}'"))

        # Update moves with their positions
        for move in Move.objects.all():
            position_name = move.name.split('-')[0]
            position = Position.objects.filter(name__icontains=position_name).first()
            if position:
                move.position = position
                move.save()
                self.stdout.write(self.style.SUCCESS(f"Updated position for move '{move.name}'"))
