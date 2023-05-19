from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import MoveHistory, ComboHistory, Move, Combo, Position, PositionHistory, Shine
from ..models import Combo, Move
from django.db import models
import logging
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
logger = logging.getLogger('salsa_app')


@login_required
def all_moves(request):
    moves = Move.objects.all()
    move_fields = [f for f in Move._meta.get_fields() if isinstance(f, models.Field)]
    context = {
        'moves': moves,
        'move_fields': move_fields,
    }
    return render(request, 'moves.html', context)


@login_required
def update_move_difficulty(request, move_id):
    move = get_object_or_404(Move, pk=move_id)
    if request.method == 'POST':
        difficulty_remembering = request.POST.get('difficulty_remembering')
        move.difficulty_remembering = difficulty_remembering
        move.save()
    return redirect('position_review')


@login_required
def move_history(request):
    move_histories = MoveHistory.objects.all()
    move_history_fields = MoveHistory._meta.get_fields()
    
    return render(request, 'move_history.html', {'move_histories': move_histories, 'move_history_fields': move_history_fields})