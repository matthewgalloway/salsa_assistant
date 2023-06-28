from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import MoveHistory, ComboHistory, Move, Combo, Position, PositionHistory, Shine
from ..utils import get_repetition_counts
from ..models import Combo, Move
from ..variable_utils import difficulty_levels_dict, memory_difficulty_dict
import logging
from ..utils import get_repetition_counts, get_review_counts
logger = logging.getLogger('salsa_app')


@login_required
def home(request):

    # Query the Move and Combo models to get the data for the charts
    repetition_counts = get_repetition_counts(request)
    review_counts = get_review_counts(request)

    # Total counts for Moves, Combos and their practiced percentage
    total_moves = Move.objects.filter(user=request.user).count()
    practiced_moves = Move.objects.filter(user=request.user, repetition__gt=0).count()
    percent_moves_practiced = round((practiced_moves / total_moves) * 100 if total_moves > 0 else 0,2)


    total_combos = Combo.objects.filter(user=request.user).count()
    practiced_combos = Combo.objects.filter(user=request.user, repetition__gt=0).count()
    percent_combos_practiced = round((practiced_combos / total_combos) * 100 if total_combos > 0 else 0,2)

    total_shines = Shine.objects.filter(user=request.user).count()
    practiced_shines = Combo.objects.filter(user=request.user, repetition__gt=0).count()
    percent_shines_practiced = round((practiced_shines / total_shines) * 100 if total_shines > 0 else 0,2)


    return render(request, 'home.html', {'repetition_counts': repetition_counts, 'review_counts': review_counts, 'total_moves': total_moves, 'percent_moves_practiced': percent_moves_practiced, 'total_combos': total_combos, 'percent_combos_practiced': percent_combos_practiced, 'total_shines': total_shines, 'percent_shines_practiced': percent_shines_practiced})
