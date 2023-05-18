from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MoveHistory, ComboHistory, Move, Combo, Position, PositionHistory, Shine
from .utils import fetch_latest_Move_or_Combo,fetch_latest_position
from .models import Combo, Move
from .variable_utils import DIFFICULTY_LEVELS, MEMORY_DIFFICULTY
from random import choice
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .forms import MoveHistoryForm, ComboHistoryForm,PositionHistoryForm
from .spaced_repition_algorithm import spaced_repetition
from datetime import datetime, timedelta
from django.db import models
from django.db.models.functions import TruncDate
from django.db.models import Count, F
import logging
from .utils import save_item_history
from django.shortcuts import get_object_or_404
logger = logging.getLogger('salsa_app')

difficulty_levels_dict = {key: value for key, value in DIFFICULTY_LEVELS}
memory_difficulty_dict = {key: value for key, value in MEMORY_DIFFICULTY}


def home(request):
    # Get the current date and time
    now = timezone.now()

    # Get the date one month from now and one month ago
    one_month_future = now + timedelta(days=30)
    one_month_past = now - timedelta(days=30)

    # Query the Move and Combo models to get the data for the charts
# Query the Move and Combo models to get the data for the charts
    repetition_counts = Move.objects.values('repetition').annotate(count=Count('id')).union(
        Combo.objects.values('repetition').annotate(count=Count('id'))).order_by('repetition')


    review_counts = (
        Move.objects
        .filter(date_next_review__range=[one_month_past, one_month_future])
        .annotate(date=TruncDate('date_next_review'))
        .values('date')
        .annotate(count=Count('id'))
        .union(
            Combo.objects
            .filter(date_next_review__range=[one_month_past, one_month_future])
            .annotate(date=TruncDate('date_next_review'))
            .values('date')
            .annotate(count=Count('id'))
        )
        .order_by('date')
    )

    # Total counts for Moves, Combos and their practiced percentage
    total_moves = Move.objects.count()
    practiced_moves = Move.objects.filter(repetition__gt=0).count()
    percent_moves_practiced = round((practiced_moves / total_moves) * 100 if total_moves > 0 else 0,2)

    total_combos = Combo.objects.count()
    practiced_combos = Combo.objects.filter(repetition__gt=0).count()
    percent_combos_practiced = round((practiced_combos / total_combos) * 100 if total_combos > 0 else 0,2)

    total_shines = Shine.objects.count()
    practiced_shines = Combo.objects.filter(repetition__gt=0).count()
    percent_shines_practiced = round((practiced_shines / total_shines) * 100 if total_shines > 0 else 0,2)

    return render(request, 'home.html', {'repetition_counts': repetition_counts, 'review_counts': review_counts, 'total_moves': total_moves, 'percent_moves_practiced': percent_moves_practiced, 'total_combos': total_combos, 'percent_combos_practiced': percent_combos_practiced, 'total_shines': total_shines, 'percent_shines_practiced': percent_shines_practiced})



def position_review(request):
    
    item = fetch_latest_position()
    if request.method == 'POST':
        form = PositionHistoryForm(request.POST)
        if form.is_valid():
            interval, easiness_factor, repetition = spaced_repetition(form)
            try:
                move = Position.objects.get(id=request.POST.get('item_id'))
                save_item_history(move, form, interval, easiness_factor, repetition)
            except Position.DoesNotExist:
                print('Error Position does not exist')

        return redirect('position_review')

    if isinstance(item, Position):
        form = PositionHistoryForm(initial={'move': item.id})

    return render(request, 'position_review.html', {'item': item, 'form': form})




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


    return render(request, 'algo_review.html', {'item': item, 'form': form, 'item_type': 'move' if isinstance(item, Move) else 'combo'})

def position_history(request):
    position_histories = PositionHistory.objects.all()
    position_history_fields = PositionHistory._meta.get_fields()
    
    return render(request, 'position_history.html', {'position_histories': position_histories, 'position_history_fields': position_history_fields})

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



def update_move_difficulty(request, move_id):
    move = get_object_or_404(Move, pk=move_id)
    if request.method == 'POST':
        difficulty_remembering = request.POST.get('difficulty_remembering')
        move.difficulty_remembering = difficulty_remembering
        move.save()
    return redirect('position_review')