from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MoveHistory, ComboHistory
from .utils import fetch_latest_Move_or_Combo
from .models import Combo, Move
from .variable_utils import DIFFICULTY_LEVELS, MEMORY_DIFFICULTY
from random import choice
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .forms import MoveHistoryForm, ComboHistoryForm
from .spaced_repition_algorithm import spaced_repetition
from datetime import datetime, timedelta
from django.db import models
import logging
from .utils import save_item_history
logger = logging.getLogger('salsa_app')

difficulty_levels_dict = {key: value for key, value in DIFFICULTY_LEVELS}
memory_difficulty_dict = {key: value for key, value in MEMORY_DIFFICULTY}



def algo_practice(request):   

    item = fetch_latest_Move_or_Combo()
    if request.method == 'POST':

        item_type = request.POST.get('item_type')

        if item_type == 'move':
            form = MoveHistoryForm(request.POST)
            if form.is_valid():
                interval, easiness_factor, repetition = spaced_repetition(form)
                try:
                    move = Move.objects.get(id=request.POST.get('item_id'))
                    save_item_history(move, form, interval, easiness_factor, repetition)
                except Move.DoesNotExist:
                    print('Error Move does not exist')

        elif item_type == 'combo':
            form = ComboHistoryForm(request.POST)
            if form.is_valid():
                interval, easiness_factor, repetition = spaced_repetition(form)
                try:
                    combo = Combo.objects.get(id=request.POST.get('item_id'))
                    save_item_history(combo, form, interval, easiness_factor, repetition)
                except Combo.DoesNotExist:
                    print('Error Combo does not exist')

        return redirect('algo_practice')

    if isinstance(item, Move):
        form = MoveHistoryForm(initial={'move': item.id})
    else:
        form = ComboHistoryForm(initial={'combo': item.id})

    return render(request, 'home.html', {'item': item, 'form': form, 'item_type': 'move' if isinstance(item, Move) else 'combo'})


def move_history(request):
    move_histories = MoveHistory.objects.all()
    move_history_fields = MoveHistory._meta.get_fields()
    
    return render(request, 'move_history.html', {'move_histories': move_histories, 'move_history_fields': move_history_fields})

def combo_history(request):
    combo_histories = ComboHistory.objects.all()
    return render(request, 'combo_history.html', {'combo_histories': combo_histories})

def all_combos(request):
    combos = Combo.objects.all()
    return render(request, 'combos.html', {"combo": combos, "difficulty_levels_dict": difficulty_levels_dict, "memory_difficulty_dict": memory_difficulty_dict})

def all_moves(request):
    moves = Move.objects.all()
    move_fields = [f for f in Move._meta.get_fields() if isinstance(f, models.Field)]
    context = {
        'moves': moves,
        'move_fields': move_fields,
    }
    return render(request, 'moves.html', context)

