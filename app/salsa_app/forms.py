from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import MoveHistory, ComboHistory, PositionHistory


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



class PositionHistoryForm(ModelForm):
    class Meta:
        model = PositionHistory
        fields = [ 'difficulty_remembering','difficulty_of_move',  'repetition', 'interval','easiness_factor_remembering','date_next_review']

    def __init__(self, *args, **kwargs):
        super(PositionHistoryForm, self).__init__(*args, **kwargs)
        self.fields['repetition'].required = False
        self.fields['interval'].required = False
        self.fields['easiness_factor_remembering'].required = False
        self.fields['date_next_review'].required = False


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user