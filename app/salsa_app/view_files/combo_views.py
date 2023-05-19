from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import MoveHistory, ComboHistory, Move, Combo, Position, PositionHistory, Shine
from ..variable_utils import difficulty_levels_dict, memory_difficulty_dict
from django.contrib.auth.decorators import login_required

@login_required
def combo_history(request):
    combo_histories = ComboHistory.objects.all()
    return render(request, 'combo_history.html', {'combo_histories': combo_histories})

@login_required
def all_combos(request):
    combos = Combo.objects.all()
    return render(request, 'combos.html', {"combo": combos, "difficulty_levels_dict": difficulty_levels_dict, "memory_difficulty_dict": memory_difficulty_dict})