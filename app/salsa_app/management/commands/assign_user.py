from django.core.management.base import BaseCommand
from django.db.models import Q
from django.contrib.auth.models import User
from salsa_app.models import Position, Move, Combo, PositionHistory, MoveHistory, ComboHistory, Shine,ShineHistory

class Command(BaseCommand):
    help = 'Fixes data integrity issues with user ids'

    def handle(self, *args, **options):
        user = User.objects.get(username='mgalloway')

        Position.objects.filter(Q(user_id='mgalloway')).update(user=user)
        Move.objects.filter(Q(user_id='mgalloway')).update(user=user)
        Combo.objects.filter(Q(user_id='mgalloway')).update(user=user)
        PositionHistory.objects.filter(Q(user_id='mgalloway')).update(user=user)
        MoveHistory.objects.filter(Q(user_id='mgalloway')).update(user=user)
        ComboHistory.objects.filter(Q(user_id='mgalloway')).update(user=user)
        Shine.objects.filter(Q(user_id='mgalloway')).update(user=user)
        ShineHistory.objects.filter(Q(user_id='mgalloway')).update(user=user)