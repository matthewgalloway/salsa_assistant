from random import choice
from .models import Move, Combo, MoveHistory, ComboHistory
from datetime import datetime, timedelta
from django.utils import timezone

def fetch_latest_Move_or_Combo():

    # Order moves and combos by date_next_review (ascending) and pick the first one
    latest_move = Move.objects.all().order_by('date_next_review').first()
    latest_combo = Combo.objects.all().order_by('date_next_review').first()

    # Select the item with the earliest date_next_review
    if latest_move and latest_combo:
        item = latest_move if latest_move.date_next_review <= latest_combo.date_next_review else latest_combo
        return item
    elif latest_move:
        item = latest_move
        return item
    elif latest_combo:
        item = latest_combo
        return item
    else:
        # If there are no eligible moves or combos, you can choose a random one or handle this case differently
        moves = list(Move.objects.all())
        combos = list(Combo.objects.all())
        item = choice(moves + combos)
        return item


def save_item_history(item,form, interval, easiness_factor, repetition):
        
        history = form.save(commit=False)
        history.date_last_practiced = timezone.now()
        history.move = item
        history.easiness_factor_remembering = easiness_factor
        history.repetition = repetition
        history.interval = interval
        history.date_next_review = history.date_last_practiced + timedelta(days=history.interval)
        history.save()


        # Update the Move instance
        item.difficulty_remembering = form.cleaned_data['difficulty_remembering']
        item.difficulty_of_move = form.cleaned_data['difficulty_of_move']
        item.easiness_factor_remembering = easiness_factor
        item.repetition = repetition
        item.interval = interval
        item.date_next_review = history.date_last_practiced + timedelta(days=item.interval)
        item.save()

