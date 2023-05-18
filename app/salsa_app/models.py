from django.db import models
from django.contrib.auth.models import User 
from .variable_utils import BASE_MOVES, HOLDS, DIFFICULTY_LEVELS, MEMORY_DIFFICULTY,default_date

class Position(models.Model):
    name = models.CharField(max_length=255)
    moves = models.ManyToManyField('Move', related_name='positions')

    difficulty_remembering = models.CharField(max_length=20,choices=MEMORY_DIFFICULTY, default=0) # Quality
    easiness_factor_remembering = models.IntegerField(default=0)
    repetition = models.IntegerField(default=0)
    interval = models.IntegerField(default=0)
    date_next_review = models.DateTimeField(default=default_date, blank=True)
        
    def __str__(self):
        return self.name
    
class Move(models.Model):
    name = models.CharField(max_length=255)
    # Remove the line below
    # position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True)
    entry_hold = models.CharField(max_length=40,choices=HOLDS, null=True, blank=True)
    exit_hold = models.CharField(max_length=40,choices=HOLDS, null=True, blank=True)

    difficulty_remembering = models.CharField(max_length=20,choices=MEMORY_DIFFICULTY, default=0) # Quality
    easiness_factor_remembering = models.IntegerField(default=0)
    date_next_review = models.DateTimeField(default=default_date, blank=True)
    difficulty_of_move = models.CharField(max_length=20,choices=DIFFICULTY_LEVELS, null=True, blank=True)
    video_link = models.CharField(max_length=255,null=True, blank=True)
    notes = models.CharField(max_length=255,null=True, blank=True)
    repetition = models.IntegerField(default=0)
    interval = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Combo(models.Model):
    name = models.CharField(max_length=255)
    Move = models.ManyToManyField(Move)
    difficulty_remembering = models.CharField(max_length=20,choices=MEMORY_DIFFICULTY, default=0) # Quality
    date_next_review = models.DateTimeField(default=default_date, blank=True)
    easiness_factor_remembering = models.IntegerField(default=0)
    difficulty_of_move = models.CharField(max_length=20,choices=DIFFICULTY_LEVELS, null=True, blank=True)
    video_link = models.CharField(max_length=255,null=True, blank=True)
    repetition = models.IntegerField(default=0)
    interval = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class ComboHistory(models.Model):
    combo = models.ForeignKey(Combo, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_last_practiced = models.DateTimeField(default=default_date, blank=True)
    date_last_practiced_social = models.DateTimeField(default=default_date, blank=True)
    date_next_review = models.DateTimeField(default=default_date, blank=True)
    difficulty_remembering = models.CharField(max_length=20,choices=MEMORY_DIFFICULTY, default=0) # Quality
    easiness_factor_remembering = models.IntegerField(default=0)
    difficulty_of_move = models.CharField(max_length=20,choices=DIFFICULTY_LEVELS, default=0)
    repetition = models.IntegerField(default=0)
    interval = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.combo}" #{self.user}"
    
class PositionHistory(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_last_practiced = models.DateTimeField(default=default_date, blank=True)
    date_last_practiced_social = models.DateTimeField(default=default_date, blank=True)
    date_next_review = models.DateTimeField(default=default_date, blank=True)
    difficulty_remembering = models.CharField(max_length=20,choices=MEMORY_DIFFICULTY, default=0) # Quality
    easiness_factor_remembering = models.IntegerField(default=0)
    difficulty_of_move = models.CharField(max_length=20,choices=DIFFICULTY_LEVELS, default=0)
    repetition = models.IntegerField(default=0)
    interval = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.combo}" #{self.user}"
    
class MoveHistory(models.Model):
    move = models.ForeignKey(Move, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_last_practiced = models.DateTimeField(default=default_date, blank=True)
    date_last_practiced_social = models.DateTimeField(default=default_date, blank=True)
    date_next_review = models.DateTimeField(default=default_date, blank=True)
    difficulty_remembering = models.CharField(max_length=20,choices=MEMORY_DIFFICULTY, default=0) # Quality
    easiness_factor_remembering = models.IntegerField(default=0)
    difficulty_of_move = models.CharField(max_length=20,choices=DIFFICULTY_LEVELS, null=True, blank=True)
    repetition = models.IntegerField(default=0)
    interval = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.move}" #{self.user}"

class Shine(models.Model):
    name = models.CharField(max_length=255)
    # Remove the line below
    # position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True)
    entry_hold = models.CharField(max_length=40,choices=HOLDS, null=True, blank=True)
    exit_hold = models.CharField(max_length=40,choices=HOLDS, null=True, blank=True)

    difficulty_remembering = models.CharField(max_length=20,choices=MEMORY_DIFFICULTY, default=0) # Quality
    easiness_factor_remembering = models.IntegerField(default=0)
    date_next_review = models.DateTimeField(default=default_date, blank=True)
    difficulty_of_move = models.CharField(max_length=20,choices=DIFFICULTY_LEVELS, null=True, blank=True)
    video_link = models.CharField(max_length=255,null=True, blank=True)
    notes = models.CharField(max_length=255,null=True, blank=True)
    repetition = models.IntegerField(default=0)
    interval = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class ShineHistory(models.Model):
    move = models.ForeignKey(Shine, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_last_practiced = models.DateTimeField(default=default_date, blank=True)
    date_last_practiced_social = models.DateTimeField(default=default_date, blank=True)
    date_next_review = models.DateTimeField(default=default_date, blank=True)
    difficulty_remembering = models.CharField(max_length=20,choices=MEMORY_DIFFICULTY, default=0) # Quality
    easiness_factor_remembering = models.IntegerField(default=0)
    difficulty_of_move = models.CharField(max_length=20,choices=DIFFICULTY_LEVELS, null=True, blank=True)
    repetition = models.IntegerField(default=0)
    interval = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.move}" #{self.user}"