from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import MoveHistory, ComboHistory, Move, Combo, Position, PositionHistory, Shine
from ..variable_utils import difficulty_levels_dict, memory_difficulty_dict
from django.contrib.auth.decorators import login_required
from django.db import models

@login_required
def combo_history(request):
    combos = Combo.objects.all()
    combo_fields = [f for f in Combo._meta.get_fields() if isinstance(f, models.Field)]
    context = {
        'combos': combos,
        'combo_fields': combo_fields,
    }
    return render(request, 'combo_history.html', context)


@login_required 
def all_combos(request):
    combos = Combo.objects.all()
    return render(request, 'combos.html', {"combo": combos, "difficulty_levels_dict": difficulty_levels_dict, "memory_difficulty_dict": memory_difficulty_dict})


