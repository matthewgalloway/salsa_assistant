from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Position, PositionHistory
from ..utils import fetch_latest_position
from ..forms import PositionHistoryForm
from ..spaced_repition_algorithm import spaced_repetition
from ..utils import save_item_history
from django.contrib.auth.decorators import login_required


@login_required
def position_review(request):
    
    item = fetch_latest_position()
    if request.method == 'POST':
        form = PositionHistoryForm(request.POST)
        if form.is_valid():
            interval, easiness_factor, repetition = spaced_repetition(form)
            try:
                move = Position.objects.get(id=request.POST.get('item_id'))
                save_item_history(move, form, interval, easiness_factor, repetition, request.user)
            except Position.DoesNotExist:
                print('Error Position does not exist')

        return redirect('position_review')

    if isinstance(item, Position):
        form = PositionHistoryForm(initial={'move': item.id})

    return render(request, 'position_review.html', {'item': item, 'form': form})

@login_required
def position_history(request):
    position_histories = PositionHistory.objects.all()
    position_history_fields = PositionHistory._meta.get_fields()
    
    return render(request, 'position_history.html', {'position_histories': position_histories, 'position_history_fields': position_history_fields})