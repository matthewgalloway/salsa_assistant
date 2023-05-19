from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MoveHistory, ComboHistory, Move, Combo, Position, PositionHistory, Shine
from .utils import fetch_latest_Move_or_Combo,fetch_latest_position
from .models import Combo, Move
from .variable_utils import difficulty_levels_dict, memory_difficulty_dict
from random import choice
from django.views.decorators.csrf import csrf_exempt
from .forms import MoveHistoryForm, ComboHistoryForm,PositionHistoryForm, UserCreationForm
from .spaced_repition_algorithm import spaced_repetition
from django.db import models
import logging
from .utils import save_item_history
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from salsa_app.view_files.home_views import home
from salsa_app.view_files.position_views import position_review, position_history
from salsa_app.view_files.move_views import all_moves, update_move_difficulty, move_history
from salsa_app.view_files.practice_views import algo_practice
from salsa_app.view_files.combo_views import combo_history, all_combos
from salsa_app.view_files.authentication_views import register

logger = logging.getLogger('salsa_app')

