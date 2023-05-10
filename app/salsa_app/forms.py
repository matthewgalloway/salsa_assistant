from django import forms

from django.forms import ModelForm
from .models import MoveHistory, ComboHistory


class MoveHistoryForm(ModelForm):
    class Meta:
        model = MoveHistory
        fields = ['difficulty_remembering', 'difficulty_of_move', 'repetition', 'interval', 'easiness_factor_remembering', 'date_next_review']
    
    def __init__(self, *args, **kwargs):
        super(MoveHistoryForm, self).__init__(*args, **kwargs)
        self.fields['repetition'].required = False
        self.fields['interval'].required = False
        self.fields['easiness_factor_remembering'].required = False
        self.fields['date_next_review'].required = False


class ComboHistoryForm(ModelForm):
    class Meta:
        model = ComboHistory
        fields = [ 'difficulty_remembering','difficulty_of_move',  'repetition', 'interval','easiness_factor_remembering','date_next_review']

    def __init__(self, *args, **kwargs):
        super(ComboHistoryForm, self).__init__(*args, **kwargs)
        self.fields['repetition'].required = False
        self.fields['interval'].required = False
        self.fields['easiness_factor_remembering'].required = False
        self.fields['date_next_review'].required = False