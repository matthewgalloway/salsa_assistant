from random import choice
from .models import Move, Combo, MoveHistory, ComboHistory, Position
from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models import Count, F
from django.db.models.functions import TruncDate
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
    
def fetch_latest_position():
    latest_position = Position.objects.all().order_by('date_next_review').first()
    if latest_position:
     return latest_position
    else:
     all_positions = list(Position.objects.all())
     return choice(all_positions)


def save_item_history(item,form, interval, easiness_factor, repetition):
        
        history = form.save(commit=False)
        history.date_last_practiced = timezone.now()
        if isinstance(item, Position):
            history.position = item
        else:
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

def get_repetition_counts(request):
    user = request.user
    repetition_counts = Move.objects.filter(user=user).values('repetition').annotate(count=Count('id')).union(
        Combo.objects.filter(user=user).values('repetition').annotate(count=Count('id'))).order_by('repetition')
        
    return repetition_counts


def get_review_counts(request):
        # Get the current date and time
    now = timezone.now()

    # Get the date one month from now and one month ago
    one_month_future = now + timedelta(days=30)
    one_month_past = now - timedelta(days=30)
    
    review_counts = (
        Move.objects
        .filter(user=request.user, date_next_review__range=[one_month_past, one_month_future])
        .annotate(date=TruncDate('date_next_review'))
        .values('date')
        .annotate(count=Count('id'))
        .union(
            Combo.objects
            .filter(user=request.user, date_next_review__range=[one_month_past, one_month_future])
            .annotate(date=TruncDate('date_next_review'))
            .values('date')
            .annotate(count=Count('id'))
        )
        .order_by('date')
    )
    return review_counts
