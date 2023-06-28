from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import MoveHistory, ComboHistory, Move, Combo, Position, PositionHistory, Shine
from ..utils import fetch_latest_Move_or_Combo
from ..models import Combo, Move
from ..forms import MoveHistoryForm, ComboHistoryForm
from ..spaced_repition_algorithm import spaced_repetition
import logging
from ..utils import save_item_history
from django.contrib.auth.decorators import login_required
logger = logging.getLogger('salsa_app')


@login_required
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
                    save_item_history(move, form, interval, easiness_factor, repetition, request.user)
                except Move.DoesNotExist:
                    print('Error Move does not exist')

        elif item_type == 'combo':
            form = ComboHistoryForm(request.POST)
            if form.is_valid():
                interval, easiness_factor, repetition = spaced_repetition(form)
                try:
                    combo = Combo.objects.get(id=request.POST.get('item_id'))
                    save_item_history(combo, form, interval, easiness_factor, repetition, request.user)
                except Combo.DoesNotExist:
                    print('Error Combo does not exist')

        return redirect('algo_practice')

    if isinstance(item, Move):
        form = MoveHistoryForm(initial={'move': item.id})
    else:
        form = ComboHistoryForm(initial={'combo': item.id})


    return render(request, 'algo_review.html', {'item': item, 'form': form, 'item_type': 'move' if isinstance(item, Move) else 'combo'})